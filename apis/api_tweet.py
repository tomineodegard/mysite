from bottle import post, request, response
import x
import uuid
import time
import os

@post("/api-tweet")
def _():
  try:
    x.disable_cache()
    x.validate_tweet()
    db = x.db()
    cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
    print("-"*50 + "cookie_user:")
    print(cookie_user)

    tweet_image = request.files.get("tweet_image", "")
    tweet_image_name = "empty"
    if tweet_image:
      tweet_image_name, _ = os.path.splitext(tweet_image.filename)

    print("-"*50 + "tweet_image_name:")
    print(tweet_image_name)


    if not cookie_user:
      raise Exception(400, "cookie_user don't exists")
    if cookie_user:
      tweet_user_fk = cookie_user["user_id"]
      
    tweet_message = request.forms.get("tweet_message", "")
    if not tweet_message and tweet_image_name == "empty": raise Exception(400, "tweet must contain text and/or image")
    tweet_image = ""

    print("-"*50 + "tweet_message:")
    print(tweet_message, tweet_image_name)


    tweet = {
      "tweet_id": str(uuid.uuid4().hex),
      "tweet_user_fk": cookie_user["user_id"],
      "tweet_created_at": int(time.time()),
      "tweet_message": tweet_message,
      "tweet_image": tweet_image,
      "tweet_updated_at": "",
      "tweet_total_retweets": "",
      "tweet_total_likes": "",
      "tweet_total_views": "",
      "tweet_total_replies": "",
    }

    values = x.get_values_from_dictionary(tweet)

    total_changes = db.execute(f"INSERT INTO tweets VALUES({values})", tweet).rowcount
    if total_changes != 1: raise Exception(400, "Please, try again")
    
    db.commit()

    return {
            "info": f"user {tweet['tweet_user_fk']} just tweeted sucesfully.", 
            "tweet_id": tweet["tweet_id"],
            "tweet_user_fk": tweet["tweet_user_fk"],
            "tweet_created_at": tweet["tweet_created_at"], 
            "tweet_message": tweet["tweet_message"],
            "tweet_image": tweet["tweet_image"], 
            "tweet_updated_at": tweet["tweet_updated_at"],
            "tweet_total_retweets": tweet["tweet_total_retweets"], 
            "tweet_total_likes": tweet["tweet_total_likes"], 
            "tweet_total_replies": tweet["tweet_total_replies"], 
            "tweet_total_views": tweet["tweet_total_views"],
            "cookie_user":cookie_user,
            }

  except Exception as ex:
    print("-"*30)
    print(ex)
    if "db" in locals(): db.rollback()
    try:
      response.status = ex.args[0]
      return {"info":ex.args[1]}
    except: response.status = 500
    return {"info":str(ex)}
  finally:
    if "db" in locals(): db.close()

