from bottle import post, request, response
import x

@post("/api-admin-activate-user")
def _():
    try:
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        if not cookie_user["user_is_active"] == 2 or not cookie_user: return {"info": "no access"}

        user_id = request.forms.get("user_id")
        print("user_id:"+"-"*30)
        print(user_id)

        db = x.db()
        total_changes = db.execute(f"""
            UPDATE users
            SET user_is_active = 1
            WHERE user_id=?
        """, (user_id,)).rowcount
        if not total_changes: raise Exception(400, "user not found")
        db.commit()

        return {"info":"ok"}
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback()
        try: # Controlled exception, usually comming from the x file
            response.status = e.args[0]
            return {"info":e.args[1]}
        except: # Something unknown went wrong
            # unknown scenario
            response.status = 500
            return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()