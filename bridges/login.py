from bottle import post, response, request
import x

@post("/login")
def _():
    x.disable_cache()
    cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
    if cookie_user:
        response.status = 303
        response.set_header("Location", "/")
        return
