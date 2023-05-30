from bottle import post, request, response
import x
import time
import traceback

@post("/api-follow")
def _():
    try:
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        if not cookie_user:raise Exception("please log in to follow someone")
        
        followed_at = int(time.time())
        followee_username = request.forms.get("followee_fk", "")
        follower_fk = cookie_user["user_id"]

        db = x.db()
        followee_fk = db.execute("SELECT user_id FROM users WHERE username = ?", (followee_username,)).fetchone()

        user_total_following = db.execute("SELECT user_total_following FROM users WHERE user_id = ?", (followee_fk["user_id"],)).fetchone()

        user_total_followers = db.execute("SELECT user_total_followers FROM users WHERE user_id=?",(followee_fk["user_id"],)).fetchone()

        follow_success = db.execute("INSERT INTO followers VALUES(?, ?, ?)", (follower_fk, followee_fk["user_id"], followed_at))
        if not follow_success:raise Exception("user not followed")

        user_is_verified = 0

        if user_total_followers["user_total_followers"] >= 3:
            rows_affected = db.execute("""
                UPDATE users 
                SET user_is_verified = 1
                WHERE user_id = ?
            """, (followee_fk,))
            if not rows_affected: raise Exception (400, "user not found")
            user_is_verified = 1
        db.commit()
        
        return {
            "info":"follow success", 
            "user_is_verified":user_is_verified,
            "user_total_followers":user_total_followers
        }
    except Exception as ex:
        print("-"*30)
        print(ex)
        if "db" in locals(): db.rollback()
        response.status = 400
        traceback.print_exc()
        return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()
