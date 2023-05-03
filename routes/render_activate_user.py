from bottle import get, template
import x


@get("/activate_user/<user_activation_key>")
def _(user_activation_key):
    try:
        db = x.db()

        user = db.execute("UPDATE users SET user_is_activated = 1 WHERE user_activation_key = ?", (user_activation_key,)).rowcount
        print("-"*50)
        print(user)
        if not user: raise Exception("User not found")
        db.commit()
        return template("activate_user", title="Activate account - Twitter")

    except Exception as ex:
        print(ex)
        return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()

