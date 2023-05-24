from bottle import request, response
import sqlite3
import pathlib 
import re

import os
import uuid
import mimetypes


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

def validate_username(taken_username):
  print("-"*50)
  print(request.forms.get("username"))
  error_taken_username = f"The username is already taken."
  error = f"The username must contain {USERNAME_MIN} to {USERNAME_MAX} and only contain letters from the english alphabet and/or numbers between 0 and 9."

  request.forms.username = request.forms.username.strip()
  print (request.forms.username)
  if len(request.forms.username) < USERNAME_MIN: raise Exception(error)
  if len(request.forms.username) > USERNAME_MAX: raise Exception(error)
  if not re.match(USERNAME_REGEX, request.forms.username): raise Exception(error)
  
  if taken_username: raise Exception(error_taken_username)
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
	error = f"The email you entered did not match our records. Please double check and try again."
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
  error = f"The password you entered did not match our records. Please double check and try again." 
  user_password = request.forms.user_password = request.forms.user_password.strip() 
  if len(request.forms.user_password) < USER_PASSWORD_MIN:
    raise Exception(error) 
  if len(request.forms.user_password) > USER_PASSWORD_MAX: 
    raise Exception(error) 
  return request.forms.user_password


def validate_user_confirm_password():
	error = f"user_password and user_confirm_password do not match"
	user_password = request.forms.get("user_password", "").strip()
	user_confirm_password = request.forms.get("user_confirm_password", "").strip()
	if user_confirm_password != user_password: raise Exception(400, error)
	return user_confirm_password



# ------------------ tweet validation
TWEET_MIN_LEN = 2
TWEET_MAX_LEN = 280

def validate_tweet():
  error = f"Tweet is not valid, the message must contain minimum {TWEET_MIN_LEN} charactes and maximum {TWEET_MAX_LEN} characters"
  if len(request.forms.message) < TWEET_MIN_LEN: raise Exception(error)
  if len(request.forms.message) > TWEET_MAX_LEN: raise Exception(error)
  return request.forms.get("message")


# ------------------ bio validation
BIO_MIN_LEN = 2
BIO_MAX_LEN = 280

def validate_user_bio():
  error = f"Bio is not valid, the bio must contain minimum {BIO_MIN_LEN} charactes and maximum {BIO_MAX_LEN} characters"
  if len(request.forms.user_bio) < BIO_MIN_LEN: raise Exception(error)
  if len(request.forms.user_bio) > BIO_MAX_LEN: raise Exception(error)
  return request.forms.get("user_bio")




# ------------------ image validation and upload
def check_mimetype_and_upload_image(field_name, path, current_image=""):
  field_name = request.files.get(f"{field_name}", "")
  _, extention = os.path.splitext(field_name.filename)

  if extention not in (".png", ".jpg", ".jpeg"): raise Exception(400, f"Images with the extention {field_name} is not allowed. Please upload a png, jpg og a jpeg.")
  image_name = str(uuid.uuid4().hex)
  image_name = image_name + extention

  ## Delete the old image
  # if not current_image == "":
  #   os.remove(f"assets/images/{path}/{current_image}")

  field_name.save(str(pathlib.Path(__file__).parent.resolve())+f"/images/{path}/{image_name}")

# DOES NOT WORK
  # mime_type = mimetypes.guess_type(str(pathlib.Path(__file__).parent.resolve())+f"/assets/images/{path}/{image_name}", strict=True)
  # if str(mime_type[0]) not in "image/jpg image/jpeg image/png":
  #   os.remove(str(pathlib.Path(__file__).parent.resolve())+f"/assets/images/{path}/{field_name_image_name}")
  #   return {"info": f"{field_name} not uploaded, because file is not allowed"}
  
  return image_name



