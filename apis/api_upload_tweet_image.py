from bottle import post, request, response
import x

##############################
@post("/api-upload-tweet-image")
def _():
    try:
        tweet_id = request.forms.get("tweet_id", "")
        print("tweet_id:", tweet_id)
        tweet_image = request.files.get("tweet_image", "")

        tweet_image = x.check_mimetype_and_upload_image("tweet_image","tweet_images", "")
        print("tweet_image:", tweet_image)

        db = x.db()
        total_changes = db.execute(f"""
            UPDATE tweets
            SET tweet_image = ?
            WHERE tweet_id = ?
        """, (tweet_image, tweet_id)).rowcount
        print("total_changes:", total_changes)
        if not total_changes: raise Exception(400, "user not found")
        db.commit()

        return {
            "info": "tweet_image uploaded to tweet ok",
            "tweet_image": tweet_image
            }
    except Exception as ex:
        print(ex)
        if "db" in locals(): db.rollback()
        try: # Controlled exception, usually comming from the x file
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except: # Something unknown went wrong
            # unknown exception
            response.status = 500
            return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()
