from bottle import post, request, response
import x
import bcrypt

##############################
@post("/api-login")
def _():
	try:
		cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
		# if the user is succesfully logged in, return message to the API
		if cookie_user: return {"info":"success login", "username":cookie_user["username"]}
		
		# Validate
		user_email = x.validate_user_email()
		user_password = x.validate_user_password()

		# Connect to database
		db = x.db()
		cookie_user = db.execute("SELECT * FROM users WHERE user_email = ? LIMIT 1", (user_email,)).fetchone()
		print("-"*50)
		print(cookie_user)
		
		activated_user = cookie_user["user_is_activated"]
		# print("-"*50)
		# print(activated_user)

		if not activated_user == 1: raise Exception(400, "You need to check your email and activate your account before you can log in.")
		
		user_is_active = cookie_user["user_is_active"]
		# print("-"*50)
		# print(user_is_active)
		# print("user_password"+"-"*50)
		# print(user_password)

		# print("cookie user[user_password]"+"-"*50)
		# print(cookie_user["user_password"])

		# print("user password encode"+"-"*50)
		# print(user_password.encode("utf-8"))
		if not user_is_active == 1: raise Exception(400, "You account is deactivated. Please contact customer support (admin@gmail.com).")
		
		if not cookie_user: raise Exception(400, "Wrong credidentials")
		if not bcrypt.checkpw(user_password.encode("utf-8"), cookie_user["user_password"]):
			raise Exception(400, "Error, the credentials you have entered are invalid")
		
		try:
			import production
			is_cookie_https = True
		except:
			is_cookie_https = False
		cookie_user.pop("user_password") # Do not put the password in the cookie
		response.set_cookie("cookie_user", cookie_user, secret=x.COOKIE_SECRET, httponly=True, secure=is_cookie_https)
		return {"info":"success login", "username":cookie_user["username"]}
	except Exception as ex:
		if "db" in locals(): db.rollback()
		print(ex)
		return {"info":str(ex)}
	finally:
		if "db" in locals(): db.close()

