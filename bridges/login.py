from bottle import post, response
import time 

@post("/login")
def _():
    cookie_user = {
        "username":"tomineodegard",
        "user_firstname":"Tomine",
        "user_lastname":"Ødegård"
    }


    response.set_cookie("cookie_user", cookie_user, secret="my-secret", httponly=True)
    response.status = 303
    response.set_header("Location", "/")
    return

