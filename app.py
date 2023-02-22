#https://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@github.com/tomineodegard/mysite.git

from bottle import default_app, get, post, template, run, response, request, static_file, view
import sqlite3
import os
import git

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
def _():
    return template("index", title="Twitter", tweets=tweets, trends=trends, people=people)



# ------------- data start
users = [
    {"profile_picture": "49b99d9e-2e60-478d-8eb4-ba7358017319.jpeg",
     "fullname": "Rihanna",
     "username": "rihanna",
     "verified": 1,
     "message": "Hey, this is my first tweet",
     "total_comments": "4",
     "total_retweets": "2",
     "total_likes": "7",
     "total_dislikes": "5",
     },
]

tweets = [
    {"profile-picture": "49b99d9e-2e60-478d-8eb4-ba7358017319.jpeg",
     "fullname": "Rihanna",
     "username": "rihanna",
     "verified": 1,
     "message": "Hey, this is my first tweet",
     "total_comments": "4",
     "total_retweets": "2",
     "total_likes": "7",
     "total_dislikes": "5",
     }
]


# ------ trending for you right side
trends = [
    {
        "title": "One",
        "total_hash": 1
    }
]

# ------ who to follow rights side
people = [
    {
        "profile_picture": "438b092d-344d-4628-a2de-afabcf5b0689.jpeg",
        "fullname": "Elon Musk",
        "username": "elonmusk",

    }
]
# ------------- data end

# -------------- get the jpeg images from the images folder
@get("/images/<filename:re:.*\.jpeg>")
def render_images(filename):
    return static_file(filename, root="./images")

# -------------- get the jpeg images from the images folder
@get("/images/<filename:re:.*\.jpg>")
def render_images(filename):
    return static_file(filename, root="./images")


# -------------- render app.css
@get("/app.css")
def render_css():
    return static_file("app.css", root=".")


# ----- route for any username, dynamically from the database
@get("/<username>")
# @view("profile")
def render_username(username):
    try:
        # ----- connect to database
        db = sqlite3.connect(os.getcwd()+"/twitter.db")

        db.row_factory = dict_factory
        user = db.execute(
            "SELECT * FROM users WHERE username=? COLLATE NOCASE", (username,)).fetchall()[0]
        # ----- Get the user's id
        user_id = user["id"]
        print("-"*50)
        print(f"user id: {user_id}")
        # ----- With that id, look up/get the respectives tweets
        tweets = db.execute(
            "SELECT * FROM tweets WHERE user_fk=?", (user_id,)).fetchall()
        print("-"*50)
        print(tweets)
        print("-"*50)

        # ----- pass the tweets to the view. Template it
        print(user)
        return template("profile", user=user)
    except Exception as ex:
        print(ex)
        return "error"
    finally:
        if "db" in locals():
            db.close()


@get("/<username>")
# @view("profile")
def render_username(username):
    try:
        # ----- connect to database
        db = sqlite3.connect(os.getcwd()+"/twitter.db")

        db.row_factory = dict_factory
        user = db.execute(
            "SELECT * FROM users WHERE username=? COLLATE NOCASE", (username,)).fetchall()[0]
        # ----- Get the user's id
        user_id = user["id"]
        print("-"*50)
        print(f"user id: {user_id}")
        # ----- With that id, look up/get the respectives tweets
        tweets = db.execute(
            "SELECT * FROM tweets WHERE user_fk=?", (user_id,)).fetchall()
        print("-"*50)
        print(tweets)
        print("-"*50)

        # ----- pass the tweets to the view. Template it
        print(user)
        return template("profile", user=user)
    except Exception as ex:
        print(ex)
        return "error"
    finally:
        if "db" in locals():
            db.close()


# -------------- the code will run on AWS
try:
  import production
  print("Server running on AWS")
  application = default_app()
  
# -------------- the code will run in local computer
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=3000, debug=True, reloader=True)
