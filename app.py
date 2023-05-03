# Github token url: https://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@github.com/tomineodegard/mysite.git

from bottle import default_app, get, post, template, run, response, request, static_file, view
import os
import sqlite3
import pathlib
import uuid
import x
import git


# ------------- connects to github and pythonanywhere
@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./mysite')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""

# ------------- makes a readable dictionary from SQLite data
def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}


# ------------- ROUTES
import routes.render_signup
import routes.render_login
import routes.render_logout
import routes.render_index
import routes.render_profile
import routes.render_activate_user



# ------------- VIEWS
import views.tweet

# ------------- APIS
import apis.api_login
import apis.api_signup
import apis.api_send_sms
import apis.api_tweet
import apis.api_follow
import apis.api_unfollow
import apis.api_activate_user


# ------------- BRIDGES
import bridges.login


# -------------- render css
@get("/app.css")
def render_css():
    return static_file("app.css", root=".")


# ----- route to upload pictures when creating a tweet
@post("/upload-picture")
def upload_picture():
    try:
        the_picture = request.files.get("picture")
        # name, ext = os.path.splitext(the_picture.filename)
        # since we dont use or need the name of this python function, we can just ignore it by calling an underscore
        _, ext = os.path.splitext(the_picture.filename)

        # print("-"*50)
        # print(name) #tomine-odegard-bw
        # print(ext) #.png
        if ext not in (".png", ".jpg", ".jpeg"):
            response.status = 400
            return "Oh no! Your chosen picture file-extension is not allowed. Please upload a png, jpg or jpeg."
        picture_name = str(uuid.uuid4().hex) #4567
        picture_name = picture_name + ext #4567.png
        the_picture.save(f"pictures/{picture_name}")  
        return ("picture-uploaded")
    except Exception as e:
        print(e)
    finally:
        pass


# -------------- get the images
@get("/images/<filename:re:.*\.jpeg>")
def render_jpeg(filename):
    return static_file(filename, root="./images")

@get("/images/<filename:re:.*\.jpg>")
def render_jpg(filename):
    return static_file(filename, root="./images")


@get("/js/<filename>")
def _(filename):
  return static_file(filename, root="js")


# -------------- the code will run on AWS
try:
  import production
  print("Server running on AWS")
  application = default_app()
  
# -------------- the code will run in local computer
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=4004, debug=True, reloader=True, server="paste")
