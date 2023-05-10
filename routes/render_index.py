from bottle import get, response, request, template
import x

@get("/")
def render_index():
    try:
        db = x.db()
        response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        response.add_header("Pragma", "no-cache")
        response.add_header("Expires", 0)
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)



        tweets = db.execute("SELECT * FROM users JOIN tweets ON tweet_user_fk = user_id ORDER BY tweet_created_at DESC").fetchall()

        trends = db.execute("SELECT * FROM trends JOIN locations ON trends.location_fk = locations.location_id").fetchall()

        if cookie_user:
            suggested_users = db.execute("SELECT * FROM users WHERE NOT user_id = ? AND user_id NOT IN (SELECT followee_fk FROM followers WHERE follower_fk = ?) ORDER BY RANDOM() LIMIT 5",(cookie_user["user_id"],cookie_user["user_id"])).fetchall()
        else: suggested_users = None   



        return template("index", title="Twitter", cookie_user=cookie_user, suggested_users=suggested_users,  trends=trends, tweets=tweets, tweet_min_len=x.TWEET_MIN_LEN, tweet_max_len=x.TWEET_MAX_LEN)
        

    except Exception as ex:
        print(ex)
        return f"{str(ex)}"


    finally:
        if "db" in locals():
            db.close()
