from bottle import post, response
import time 

@post("/login")
def _():
    cookie_user = {
        "user_name":"tomineodegard",
        "user_first_name":"Tomine",
        "user_last_name":"Ødegård"
    }


    response.set_cookie("cookie_user", cookie_user, secret="my-secret", httponly=True)
    response.status = 303
    response.set_header("Location", "/")
    return

