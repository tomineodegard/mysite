from bottle import get, template


@get("/forgot_password")
def _():
	return template("forgot_password", title="Forgot password - Twitter")