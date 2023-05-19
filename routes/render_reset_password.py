from bottle import get, template
import x


@get("/reset_password/<user_reset_password_key>")
def _(user_reset_password_key):
    try:
        db = x.db()

        # user = db.execute("UPDATE users SET user_password = ? WHERE username = ? AND user_email = ?", (user_activation_key,)).rowcount
        # print("-"*50)
        # print(user)
        # if not user: raise Exception("User not found")
        # db.commit()
        return template("reset_password", title="Reset password - Twitter")
    except Exception as ex:
        print(ex)
        return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()