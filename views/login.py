from bottle import get, template

# ------------------
@get("/login")
def _():
	return template("login", title="Log in - Twitter")











