# Github token url: https://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@github.com/tomineodegard/mysite.git

from bottle import default_app, get, post, template, run, response, request, static_file, view
import os
import sqlite3
import pathlib
import uuid
import x
import git

# -------------  route to render the index
@get("/")
def render_index():
    try:
        response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        response.add_header("Pragma", "no-cache")
        response.add_header("Expires", 0)
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)

        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        db.row_factory = dict_factory
        tweets = db.execute("SELECT * FROM users JOIN tweets ON tweet_user_fk = user_id ORDER BY tweet_created_at DESC").fetchall()
        trends = db.execute("SELECT * FROM trends JOIN locations ON trends.location_fk = locations.location_id").fetchall()
        suggested_users = db.execute("SELECT * FROM suggested_users").fetchall()
        return template("index", title="Twitter", cookie_user=cookie_user, suggested_users=suggested_users, trends=trends, tweets=tweets, tweet_min_len=x.TWEET_MIN_LEN, tweet_max_len=x.TWEET_MAX_LEN)
        

    except Exception as ex:
        print(ex)
        return str(ex)


    finally:
        if "db" in locals():
            db.close()



# ----- route to render any username, dynamically from the database
@get("/<username>")
def render_username(username):
    try:

        # ----- connect to the twitter database
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        db.row_factory = dict_factory
        user = db.execute("SELECT * FROM users WHERE username=? COLLATE NOCASE", (username,)).fetchall()[0]
        trends = db.execute("SELECT * FROM trends JOIN locations ON trends.location_fk = locations.location_id").fetchall()
        suggested_users = db.execute("SELECT * FROM suggested_users").fetchall()
        # ----- Get the user's id
        user_id = user["user_id"]
        print("-"*50)
        print(f"user id: {user_id}")
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)


        # ----- With that id, look up/get all the respectives tweets
        tweets = db.execute("SELECT * FROM tweets WHERE tweet_user_fk=? ORDER BY tweet_created_at ASC LIMIT 10", (user_id,)).fetchall()
        # print("-"*50)
        # print(tweets)
        # print("-"*50)

        # ----- pass the tweets to the view. Template it
        print(user)
        return template("profile", title="Twitter", cookie_user=cookie_user, trends=trends, user=user, tweets=tweets, suggested_users=suggested_users)

    except Exception as ex:
        print("-"*50)
        print(ex)
        print("-"*50)
        return "error"

    finally:
        if "db" in locals():
            db.close()




# ----- route to render the verification of a new user
@get("/activate_user/<user_activation_key>")
def _(user_activation_key):
    try:
        db = x.db()

        user = db.execute("UPDATE users SET user_is_activated = 1 WHERE user_activation_key = ?", (user_activation_key,)).rowcount
        print("-"*50)
        print(user)
        if not user: raise Exception("User not found")
        db.commit()
        return template("activate_user", title="Activate account - Twitter")

    except Exception as ex:
        print(ex)
        return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()



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

# ------------- render login
@get("/login")
def _():
    return template("login")



# ------------- ROUTES
import routes.login
import routes.logout
import routes.signup



# ------------- VIEWS
import views.tweet
import views.test_follow

# ------------- APIS
import apis.api_login
import apis.api_signup
import apis.api_send_sms
import apis.api_tweet
import apis.api_follow
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
  run(host="127.0.0.1", port=4000, debug=True, reloader=True, server="paste")
