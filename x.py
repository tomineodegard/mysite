from bottle import request
import sqlite3
import pathlib 
import re

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################
def db():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
    db.row_factory = dict_factory
    return db
  except Exception as ex:
    print(ex)
  finally:
    pass



##############################

TWEET_MIN_LEN = 2
TWEET_MAX_LEN = 280

def validate_tweet():
  error = f"Tweet is not valid, the message must contain minimum {TWEET_MIN_LEN} charactes and maximum {TWEET_MAX_LEN} characters"
  if len(request.forms.message) < TWEET_MIN_LEN: raise Exception(error)
  if len(request.forms.message) > TWEET_MAX_LEN: raise Exception(error)
  return request.forms.get("message")


##############################
USERNAME_MIN = 4
USERNAME_MAX = 15
# english letters only, lower case and uppercase and numbers from 0 to 9 including underscore
USERNAME_REGEX = "^[a-zA-Z0-9_]*$"

def validate_username():
  print("-"*50)
  print(request.forms.username)
  
  error = f"username must contain {USERNAME_MIN} to {USERNAME_MAX} english letters or number from 0 to 9"
  request.forms.username = request.forms.username.strip()
  if len(request.forms.username) < USERNAME_MIN: raise Exception(error)
  if len(request.forms.username) > USERNAME_MAX: raise Exception(error)
  if not re.match(USERNAME_REGEX, request.forms.username): raise Exception(error)

  # ensure_ascii=True







