from bottle import get, template


@get("/signup")
def _():
    return template("signup", title="Signup - Twitter")