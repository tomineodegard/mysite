from bottle import post, request, response
import x
import time
import traceback

@post("/api-follow")
def _():
    try:
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        if not cookie_user:raise Exception("please log in to follow someone")
        
        follower_fk = cookie_user["user_id"]
        followee_fk = request.forms.get("followee_fk", "")
        print("followee_fk:"+"-"*50)
        print(followee_fk)
        
        followed_at = int(time.time())

        db = x.db()
        # print("follower_fk:"+"-"*50)
        # print(follower_fk)

        follow_success = db.execute("INSERT INTO followers VALUES(?, ?, ?)", (follower_fk, followee_fk, followed_at))
        if not follow_success: raise Exception (400, "user not followed")

        user_total_followers = db.execute("SELECT user_total_followers FROM users WHERE user_id=?",(followee_fk,)).fetchone()
        user_total_following = db.execute("SELECT user_total_following FROM users WHERE user_id=?",(followee_fk,)).fetchone()

        # print("user_total_followers:"+"-"*50)
        # print(user_total_followers)

        # ---- Check if the user has more than 3 followers aka is verified
        user_is_verified = 0
        if user_total_followers["user_total_followers"] >= 3:
            total_changes = db.execute("UPDATE users SET user_is_verified = 1 WHERE user_id = ?", (followee_fk,)).rowcount
            # print("total_changes:"+"-"*50)
            # print(total_changes)

            if not total_changes: raise Exception (400, "user not found")
            user_is_verified = 1
        db.commit()
        
        return {
            "info": f"user with id {follower_fk} is unfollowing {followee_fk}", 
            "follower_fk": follower_fk,
            "followee_fk": followee_fk,
            "user_is_verified": user_is_verified,
            "user_total_followers": user_total_followers["user_total_followers"],
            "user_total_following": user_total_following["user_total_following"]
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
