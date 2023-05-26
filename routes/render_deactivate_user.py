from bottle import get, template, request
import x


@get("/deactivate_user/<user_deactivate_key>")
def _(user_deactivate_key):
    try:
        db = x.db()
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        print("Cookie user: " +"-"*50)
        print(cookie_user)

        print("user_deactivate_key: " +"-"*50)
        print(user_deactivate_key)
        
        return template("confirm_deactivate_account", title="Deactivate user - Twitter", user_deactivate_key=user_deactivate_key, cookie_user=cookie_user)
    except Exception as ex:
        print("Exection: " +"-"*50)
        print(ex)
        return f"{str(ex)}"

    finally:
        if "db" in locals():
            db.close()