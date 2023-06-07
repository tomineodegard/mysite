from bottle import get, template, request
import x


@get("/settings")
def _():
	
    try:
        db = x.db()
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        print("Cookie user: " +"-"*50)
        print(cookie_user)

        return template("settings", title="Settings - Twitter", cookie_user=cookie_user)
    except Exception as ex:
        print("Exception: " +"-"*50)
        print(ex)
        return f"{str(ex)}"

    finally:
        if "db" in locals():
            db.close()










