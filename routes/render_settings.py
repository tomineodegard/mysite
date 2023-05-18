from bottle import get, template, request
import x

@get("/settings")
def render_settings(username):
    try:
        db = x.db()
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        if cookie_user:
            user = db.execute("SELECT * FROM users WHERE username=? COLLATE NOCASE", (username,)).fetchall()[0]

        print("cookie user is:" + "-"*50)
        print(cookie_user)
        
        db.commit()
        return template("settings", title="Settings - Twitter", user=user)

    except Exception as ex:
        print(ex)
        return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()












