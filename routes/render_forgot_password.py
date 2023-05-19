from bottle import get, template
import x


@get("/forgot_password")
def _():
	return template("forgot_password", title="Forgot password - Twitter")