from bottle import get, response, request, template
import x

# ----- route to render any username, dynamically from the database
@get("/<username>")
def render_username(username):
    try:
        # ----- connect to the twitter database
        db = x.db()
        user = db.execute("SELECT * FROM users WHERE username=? COLLATE NOCASE", (username,)).fetchall()[0]
        trends = db.execute("SELECT * FROM trends JOIN locations ON trends.location_fk = locations.location_id").fetchall()
        suggested_users = db.execute("SELECT * FROM suggested_users").fetchall()
        # ----- Get the user's id
        user_id = user["user_id"]
        print("I am here - app.py" +"*"*50)
        # print(f"user id: {user_id}")
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)


        # ----- With that id, look up/get all the respectives tweets
        tweets = db.execute("SELECT * FROM tweets WHERE tweet_user_fk=? ORDER BY tweet_created_at ASC LIMIT 10", (user_id,)).fetchall()
        # print("-"*50)
        # print(tweets)
        # print("-"*50)

        follow = db.execute("SELECT * FROM followers WHERE follower_fk=? AND followee_fk=?", (cookie_user["user_id"], user_id)).fetchall()
        # print("follow"+"-"*50)
        # print(follow)

        # ----- pass the tweets to the view. Template it
        print(user)
        return template("profile", title="Twitter", cookie_user=cookie_user, trends=trends, user=user, tweets=tweets, suggested_users=suggested_users, follow=follow)

    except Exception as ex:
        print("-"*50)
        print(ex)
        print("-"*50)
        return f"{str(ex)}"

    finally:
        if "db" in locals():
            db.close()
