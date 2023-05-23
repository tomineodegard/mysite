from bottle import get, template, request
import x


@get("/reset_password/<user_reset_password_key>")
def _(user_reset_password_key):
    try:
        return template("reset_password", title="Reset password - Twitter", user_reset_password_key=user_reset_password_key)
    except Exception as ex:
        print(ex)
        return {"info":str(ex)}
    finally:
       pass