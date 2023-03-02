from bottle import post, request, response
import x
import uuid
import time

@post("/tweet")
def _():
  try:
    x.validate_tweet()
    db = x.db()
    # tweet_id = str(uuid.uuid4()).replace("-","")
    tweet_id = str(uuid.uuid4().hex)
    tweet_user_fk = "ebb0d9d74d6c4825b3e1a1bcd73ff49a"
    tweet_created_at = int(time.time())
    tweet_message = request.forms.get("message")
    tweet_image = ""
    tweet_updated_at = ""
    tweet_total_retweets = ""
    tweet_total_likes = ""
    tweet_total_dislikes = ""
    tweet_total_views = ""
    tweet_total_replies = ""
    db.execute("INSERT INTO tweets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (tweet_id, tweet_message, tweet_image, tweet_created_at, tweet_user_fk, tweet_updated_at, tweet_total_retweets, tweet_total_likes, tweet_total_dislikes, tweet_total_views, tweet_total_replies))
    db.commit()
    return {"info":"ok", "tweet_id":tweet_id}

  except Exception as ex:
    print("#"*30)
    print(ex)
    response.status = 400
    return {"info":str(ex)}
  finally:
    if "db" in locals(): db.close()
