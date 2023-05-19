from bottle import post, request
import x

@post("/api-update-user")
def _():
    try:
        db = x.db()
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        user_id = cookie_user["user_id"]

        new_user_firstname = x.validate_user_firstname()
        new_user_bio = x.validate_user_bio()
        new_user_lastname = ""

        input_new_user_lastname = request.forms.get("user_lastname")
        # print("input_new_user_lastname is this:"+"-"*50)
        # print(input_new_user_lastname)
        if input_new_user_lastname:
            print("input_new_user_lastname is TRUE:"+"-"*50)
            print(input_new_user_lastname)
            new_user_lastname = x.validate_user_lastname()
        


        update_user = db.execute("UPDATE users SET user_firstname = ?, user_lastname = ?, user_bio = ? WHERE user_id = ?", (new_user_firstname, new_user_lastname, new_user_bio, user_id)).rowcount
        if not update_user:raise Exception("Something went wrong")

        db.commit()

        return {"info":"ok"}
    except Exception as ex:
        print(ex)

        return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()