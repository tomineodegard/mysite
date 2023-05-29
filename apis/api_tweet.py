from bottle import post, request, response
import x
import uuid
import time

@post("/api-tweet")
def _():
  try:
    print("HELLO?")
    x.disable_cache()
    x.validate_tweet()
    db = x.db()
    cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
    print("-"*50 + "cookie_user:")
    print(cookie_user)
    tweet_id = str(uuid.uuid4().hex)
    tweet_user_fk = cookie_user["user_id"]
    tweet_created_at = int(time.time())
    tweet_message = request.forms.get("message")
    tweet_image = ""
    tweet_updated_at = ""
    tweet_total_retweets = ""
    tweet_total_likes = ""
    tweet_total_dislikes = ""
    tweet_total_views = ""
    tweet_total_replies = ""
    
    db.execute("INSERT INTO tweets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (tweet_id, tweet_user_fk, tweet_created_at, tweet_message, tweet_image, tweet_updated_at, tweet_total_retweets, tweet_total_likes, tweet_total_dislikes, tweet_total_views, tweet_total_replies))
    db.commit()
    return {"info":"ok", "cookie_user":cookie_user, "tweet_id":tweet_id, "tweet_user_fk":tweet_user_fk, "tweet_created_at":tweet_created_at, "tweet_message":tweet_message, "tweet_image":tweet_image, "tweet_updated_at":tweet_updated_at,"tweet_total_retweets":tweet_total_retweets,"tweet_total_likes":tweet_total_likes, "tweet_total_dislikes":tweet_total_dislikes, "tweet_total_views":tweet_total_views, "tweet_total_replies":tweet_total_replies  }

  except Exception as ex:
    print("-"*30)
    print(ex)
    response.status = 400
    return {"info":str(ex)}
  finally:
    if "db" in locals(): db.close()