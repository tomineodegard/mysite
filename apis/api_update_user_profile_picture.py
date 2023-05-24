from bottle import post, request, response
import x

@post("/api-update-user-profile-picture")

def _():
    try:
        db = x.db()
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        # if not cookie_user:raise Exception(400, "cookie_user does not exist")

        if cookie_user:
            user_id = cookie_user["user_id"]
            user_profile_picture = cookie_user["user_profile_picture"]
        print("I am here --------------------")

        
        if not cookie_user:
            user_id = "2f9214d6266e4a96a95bb6a5fb7d1a47"
            user_profile_picture = ""
            
        user_profile_picture_image_name = x.check_mimetype_and_upload_image("user_profile_picture", "profilepictures", user_profile_picture)


        rows_affected = db.execute(f"""
            UPDATE users
            SET user_profile_picture = ?
            WHERE user_id = ?
        """, (user_profile_picture_image_name, user_id)).rowcount

        print("-"*50+"rows_affected:")
        print(rows_affected)

        if not rows_affected: raise Exception(400, "user not found")
        user = db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
        db.commit()

        try: 
            import production
            is_cookie_https = True
        except:
            is_cookie_https = False
        user.pop("user_password") # Do not put the password in the cookie
        response.set_cookie("cookie_user", user, secret=x.COOKIE_SECRET, httponly=True, secure=is_cookie_https)


        return {
            "info": "user_profile_picture uploaded",
            "user_profile_picture": user_profile_picture_image_name
            }
    except Exception as ex:
        print(ex)
        if "db" in locals(): db.rollback()
        try: # Controlled exception, usually comming from the x file
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except: # Something unknown went wrong
            # unknown exception
            response.status = 500
            return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()