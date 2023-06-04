import sqlite3
import uuid
import pathlib
import time
import random

# ------------------
def get_values_from_dictionary(dictionary):
    values = ""
    for key in dictionary:
        values += f":{key},"
    values.rstrip(",")
    return values.rstrip(",")	

# ------------------ Make the dict to "json"
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}


# ------------------ Connect to the database
def db():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.parent.resolve())+"/twitter.db")
    db.execute("PRAGMA foreign_keys = ON")
    db.row_factory = dict_factory
    return db
  except Exception as ex:
    print(ex)
  finally:
    pass

db = db()

elon_tweet_image = "94e041777c28495cbf62de59b75fa2d7.jpeg"
rihanna_tweet_image = "8432451bc484471fac3788f2ac70ad26.jpeg"
tomine_tweet_image = "3f19d64fe81b478bb93a1c6346f7a482.jpeg"
tomine_tweet_image_dog = "a2d661d8d8dd49119bf80e5515066962.jpg"
        
tweet_elon = {
        "tweet_id": "49c29377eda74912b854ffd818bf34cf",
        "tweet_user_fk": "64c3b11f947248719fc0f7e97fb5cdb0",
        "tweet_created_at": int(time.time()) - random.randint(0, 1000000),
        "tweet_message": "ChatGPT to the mainstream media",
        "tweet_image": elon_tweet_image,
        "tweet_updated_at": 0, 
        "tweet_total_retweets": 0,
        "tweet_total_likes": 0,
        "tweet_total_views": 0,
        "tweet_total_replies": 0,
    }

tweet_rihanna = {
        "tweet_id": "8909c8dacad44b8cb4cc3b2ce0b4e999",
        "tweet_user_fk": "dd41b0e3eeb94f3c9d4304ba44ff198c",
        "tweet_created_at": int(time.time()) - random.randint(0, 1000000),
        "tweet_message": "my son so fine! Idc idc idc! How crazy both of my babies were in these photos and mommy had no clue ❤️❤️ thank you so much @edward_enninful and @inezandvinoodh for celebrating us as a family!",
        "tweet_image": rihanna_tweet_image,
        "tweet_updated_at": 0, 
        "tweet_total_retweets": 0,
        "tweet_total_likes": 0,
        "tweet_total_views": 0,
        "tweet_total_replies": 0,
    }
        
tweet_tomine = {
        "tweet_id": "2002ffd57fb642da8a413052f378c717",
        "tweet_user_fk": "2f9214d6266e4a96a95bb6a5fb7d1a47",
        "tweet_created_at": int(time.time()) - random.randint(0, 1000000),
        "tweet_message": "Hello world, I am tweeting!",
        "tweet_image": tomine_tweet_image,
        "tweet_updated_at": 0, 
        "tweet_total_retweets": 0,
        "tweet_total_likes": 0,
        "tweet_total_views": 0,
        "tweet_total_replies": 0,
    }


tweet_tomine_dog = {
        "tweet_id": "db8d0707316d4ac99cb5cd9551a61e1f",
        "tweet_user_fk": "2f9214d6266e4a96a95bb6a5fb7d1a47",
        "tweet_created_at": int(time.time()) - random.randint(0, 1000000),
        "tweet_message": "Have you seen a more adorable thing???",
        "tweet_image": tomine_tweet_image_dog,
        "tweet_updated_at": 0, 
        "tweet_total_retweets": 0,
        "tweet_total_likes": 0,
        "tweet_total_views": 0,
        "tweet_total_replies": 0,
    }



values = get_values_from_dictionary(tweet_elon)
print(values)
db.execute(f"INSERT INTO tweets VALUES({values})", tweet_tomine).rowcount
db.execute(f"INSERT INTO tweets VALUES({values})", tweet_tomine_dog).rowcount
db.execute(f"INSERT INTO tweets VALUES({values})", tweet_elon).rowcount
db.execute(f"INSERT INTO tweets VALUES({values})", tweet_rihanna).rowcount

db.commit()

db.close()
