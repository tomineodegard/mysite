from bottle import delete, request, response
import x
import traceback


@delete("/api-unfollow")
def _():
    try:
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        if not cookie_user:raise Exception("please log in to unfollow someone")
        unfollower_fk = cookie_user["user_id"]
        unfollowee_fk = request.forms.get("unfollowee_fk", "")

        print("unfollow unfollowee_fk:" + "-"*30)
        print(unfollowee_fk)

        db = x.db()

        unfollow_success = db.execute("DELETE FROM followers WHERE follower_fk=? AND followee_fk=?", (unfollower_fk, unfollowee_fk)).rowcount
        # print("unfollow_success:"+"-"*50)
        # print(unfollow_success)
        if unfollow_success != 1: raise Exception(400, "oh no, user not unfollowed successfully")

        user_total_followers = db.execute("SELECT user_total_followers FROM users WHERE user_id=?",(unfollowee_fk,)).fetchone()
        user_total_following = db.execute("SELECT user_total_following FROM users WHERE user_id=?",(unfollowee_fk,)).fetchone()

        # ---- Check if the user has more than 3 followers aka is verified
        user_is_verified = 0
        if user_total_followers["user_total_followers"] < 3:
            total_changes = db.execute("UPDATE users SET user_is_verified = 0 WHERE user_id = ?", (unfollowee_fk,)).rowcount
            if not total_changes: raise Exception (400, "user not found")
            user_is_verified = 0

        db.commit()
        return {
            "info":f"user with id {unfollower_fk} is unfollowing {unfollowee_fk}",
            "unfollower_fk":unfollower_fk,
            "unfollowee_fk":unfollowee_fk,
            "user_is_verified":user_is_verified,
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
