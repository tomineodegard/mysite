from bottle import delete, request, response
import x


@delete("/api-unfollow")
def _():
    try:
        db = x.db()
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        if not cookie_user:raise Exception("please log in to unfollow someone")

        unfollower_fk = cookie_user["user_id"]

        unfollowee_username = request.forms.get("unfollowee_fk", "")
        print(unfollowee_username)
        unfollowee_fk = db.execute("SELECT user_id FROM users WHERE username = ?", (unfollowee_username,)).fetchone()


        unfollow_success = db.execute("DELETE FROM followers WHERE follower_fk=? AND followee_fk=?", (unfollower_fk, unfollowee_fk["user_id"]))
        if not unfollow_success:raise Exception("oh no, user not unfollowed successfully")

        print("unfollowee_username is" + "-"*30)
        print(unfollowee_username)
        print("unfollowee_fk is" + "-"*30)

        db.commit()
        return {"info":f"user with id {unfollower_fk} is unfollowing {unfollowee_username}"}
    
    except Exception as ex:
        print("-"*30)
        print(ex)
        response.status = 400
        return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()
