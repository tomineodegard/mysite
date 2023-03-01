#https://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@github.com/tomineodegard/mysite.git

from bottle import default_app, get, post, template, run, response, request, static_file, view
import os
import sqlite3
import pathlib
import uuid

@get("/js/<filename>")
def _(filename):
  return static_file(filename, "js")



# ------------- connects to github and pythonanywhere
@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./mysite')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""

# ------------- makes a dictionary from SQLite data
def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}


# ------------- render index
@get("/")
def render_index():
    try:
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        db.row_factory = dict_factory
        tweets = db.execute("SELECT * FROM tweets JOIN users ON tweets.user_fk = users.user_id ORDER BY created_at ASC").fetchall()
        trends = db.execute("SELECT * FROM trends").fetchall()
        suggested_users = db.execute("SELECT * FROM suggested_users").fetchall()
        return template("index", title="Twitter", suggested_users=suggested_users, trends=trends, tweets=tweets)
        

    except Exception as ex:
        print(ex)
        return str(ex)


    finally:
        if "db" in locals():
            db.close()



# ----- render any username, dynamically from the database
@get("/<username>")
# @view("profile")
def render_username(username):
    try:
        # ----- connect to the twitter database
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        db.row_factory = dict_factory
        user = db.execute("SELECT * FROM users WHERE username=? COLLATE NOCASE", (username,)).fetchall()[0]
        trends = db.execute("SELECT * FROM trends").fetchall()
        suggested_users = db.execute("SELECT * FROM suggested_users").fetchall()
        # ----- Get the user's id
        user_id = user["user_id"]
        print("-"*50)
        print(f"user id: {user_id}")

        # ----- With that id, look up/get all the respectives tweets
        tweets = db.execute("SELECT * FROM tweets WHERE user_fk=? ORDER BY created_at ASC", (user_id,)).fetchall()
        print("-"*50)
        print(tweets)
        print("-"*50)

        # ----- pass the tweets to the view. Template it
        print(user)
        return template("profile", title="Twitter", trends=trends, user=user, tweets=tweets, suggested_users=suggested_users)

    except Exception as ex:
        print("-"*50)
        print(ex)
        print("-"*50)
        return "error"

    finally:
        if "db" in locals():
            db.close()


##############################
# VIEWS
import views.tweet

##############################
# APIS
import apis.api_tweet


# -------------- render css
@get("/app.css")
def render_css():
    return static_file("app.css", root=".")


# -------------- get the images
@get("/images/<filename:re:.*\.jpeg>")
def render_jpeg(filename):
    return static_file(filename, root="./images")

@get("/images/<filename:re:.*\.jpg>")
def render_jpg(filename):
    return static_file(filename, root="./images")



###################### -------------- the code will run on AWS
try:
  import production
  print("Server running on AWS")
  application = default_app()
  
# -------------- the code will run in local computer
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=4000, debug=True, reloader=True)
