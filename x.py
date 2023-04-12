from bottle import request, response
import sqlite3
import pathlib 
import re

COOKIE_SECRET = "my_secret_cookie_key"


# ------------------
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

# ------------------
def db():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
    db.row_factory = dict_factory
    db.execute("PRAGMA foreign_keys = ON")
    return db
  except Exception as ex:
    print(ex)
  finally:
    pass


# ------------------
def disable_cache():
    response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)    

# ------------------
def validate_user_logged_in():
    cookie_user = request.get_cookie("cookie_user", secret=COOKIE_SECRET)
    if cookie_user is None: raise Exception(400, "user must login")
    return cookie_user


# ------------------ username validation
USERNAME_MIN = 4
USERNAME_MAX = 15
USERNAME_REGEX = "^[a-zA-Z0-9_]*$"

def validate_username():
  print("-"*50)
  print(request.forms.get("username"))
  
  error = f"username must contain {USERNAME_MIN} to {USERNAME_MAX} english letters or number from 0 to 9"
  request.forms.username = request.forms.username.strip()
  print ("*" * 50 + "HELLO???")
  print (request.forms.username)
  if len(request.forms.username) < USERNAME_MIN: raise Exception(error)
  if len(request.forms.username) > USERNAME_MAX: raise Exception(error)
  if not re.match(USERNAME_REGEX, request.forms.username): raise Exception(error)
  return request.forms.username


# ------------------ firstname validation
USER_FIRSTNAME_MIN = 4
USER_FIRSTNAME_MAX = 15
USER_FIRSTNAME_REGEX = "^[a-zA-Z]*$"

def validate_user_firstname():
  print("user firstname:" + "-"*50)
  print(request.forms.user_firstname)
  
  error = f"user_firstname must contain {USER_FIRSTNAME_MIN} to {USER_FIRSTNAME_MAX} english letters"
  validated_firstname = request.forms.user_firstname = request.forms.user_firstname.strip()
  if len(request.forms.user_firstname) < USER_FIRSTNAME_MIN: raise Exception(error)
  if len(request.forms.user_firstname) > USER_FIRSTNAME_MAX: raise Exception(error)
  if not re.match(USER_FIRSTNAME_REGEX, request.forms.user_firstname): raise Exception(error)
  return validated_firstname


# ------------------ lastname validation
USER_LASTNAME_MIN = 4
USER_LASTNAME_MAX = 15
USER_LASTNAME_REGEX = "^[a-zA-Z]*$"

def validate_user_lastname():
  print("user lastname:" + "-"*50)
  print(request.forms.user_lastname)
  
  error = f"user_lastname must contain {USER_LASTNAME_MIN} to {USER_LASTNAME_MAX} english letters"
  validated_lastname = request.forms.user_lastname = request.forms.user_lastname.strip()
  if len(request.forms.user_lastname) < USER_LASTNAME_MIN: raise Exception(error)
  if len(request.forms.user_lastname) > USER_LASTNAME_MAX: raise Exception(error)
  if not re.match(USER_LASTNAME_REGEX, request.forms.user_lastname): raise Exception(error)
  return validated_lastname


# ------------------ email validation
USER_EMAIL_MIN = 6
USER_EMAIL_MAX = 100
USER_EMAIL_REGEX = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"

def validate_user_email():
	error = f"user_email invalid"
	user_email = request.forms.get("user_email", "")        
	user_email = user_email.strip()
	if len(user_email) < USER_EMAIL_MIN : raise Exception(400, error)
	if len(user_email) > USER_EMAIL_MAX : raise Exception(400, error)  
	if not re.match(USER_EMAIL_REGEX, user_email): raise Exception(400, error)
	return user_email


# ------------------ password validation
USER_PASSWORD_MIN = 6
USER_PASSWORD_MAX = 50

def validate_user_password():
  password = request.forms.user_password 
  print(password) 
  error = f"user_password {USER_PASSWORD_MIN} to {USER_PASSWORD_MAX} characters" 
  request.forms.user_password = request.forms.user_password.strip() 
  if len(request.forms.user_password) < USER_PASSWORD_MIN:
    raise Exception(error) 
  if len(request.forms.user_password) > USER_PASSWORD_MAX: 
    raise Exception(error) 
  return request.forms.user_password


# ------------------ tweet validation
TWEET_MIN_LEN = 2
TWEET_MAX_LEN = 280

def validate_tweet():
  error = f"Tweet is not valid, the message must contain minimum {TWEET_MIN_LEN} charactes and maximum {TWEET_MAX_LEN} characters"
  if len(request.forms.message) < TWEET_MIN_LEN: raise Exception(error)
  if len(request.forms.message) > TWEET_MAX_LEN: raise Exception(error)
  return request.forms.get("message")





