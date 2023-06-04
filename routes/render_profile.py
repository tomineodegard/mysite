from bottle import get, response, request, template
import x

@get("/<username>")
def render_username(username):
    try:
        db = x.db()
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        user = db.execute("SELECT * FROM users WHERE username=? COLLATE NOCASE", (username,)).fetchall()[0]
        print("Cookie user: " +"-"*50)
        print(cookie_user)

        if cookie_user:
            suggested_users = db.execute("SELECT * FROM users WHERE NOT user_id = ? AND user_id NOT IN (SELECT followee_fk FROM followers WHERE follower_fk = ?) ORDER BY RANDOM() LIMIT 5",(cookie_user["user_id"],cookie_user["user_id"])).fetchall()
        else: suggested_users = None   
        # print("Suggested user: " +"-"*50)
        # print(suggested_users)

        trends = db.execute("SELECT * FROM trends JOIN locations ON trends.location_fk = locations.location_id").fetchall()


        user_id = user["user_id"]
        tweets = db.execute("SELECT * FROM tweets WHERE tweet_user_fk=? ORDER BY tweet_created_at DESC LIMIT 10", (user_id,)).fetchall()    
        # print("User: " +"-"*50)
        # print(user)
        # 
        if cookie_user:
            user_is_admin = cookie_user["user_is_active"] == 2
            if not user_is_admin: raise Exception(400, "You are not admin.")
        else: user_is_admin = None   


        if cookie_user:
            follow = db.execute("SELECT * FROM followers WHERE follower_fk=? AND followee_fk=?", (cookie_user["user_id"], user_id)).fetchall()
        else: follow = None

        return template("profile", title="Twitter", user_is_admin=user_is_admin, cookie_user=cookie_user, trends=trends, user=user, tweets=tweets, suggested_users=suggested_users, follow=follow, user_id=user_id)

    except Exception as ex:
        print("Exection: " +"-"*50)
        print(ex)
        return f"{str(ex)}"

    finally:
        if "db" in locals():
            db.close()
