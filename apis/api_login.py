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
		print("-"*50)
		print(activated_user)

		if not activated_user == "1": raise Exception(400, "You need to check your email and activate your account before you can log in.")
		
		if not cookie_user: raise Exception(400, "Wrong credidentials")
		if not bcrypt.checkpw(user_password.encode("utf-8"), cookie_user["user_password"]):
			raise Exception(400, "Error, the credentials you have entered are invalid")
		
		# if cookie_user["user_is_active"] == 0:
		# 	raise Exception(400, "User is no longer activate, check your email or contact support.")
        
		try:
			import production
			is_cookie_https = True
		except:
			is_cookie_https = False
		cookie_user.pop("user_password") # Do not put the password in the cookie
		response.set_cookie("cookie_user", cookie_user, secret=x.COOKIE_SECRET, httponly=True, secure=is_cookie_https)
		return {"info":"success login", "username":cookie_user["username"]}
	except Exception as e:
		print(e)
		try: # Controlled exception, usually comming from the x file
			response.status = e.args[0]
			return {"info":e.args[1]}
		except: # Something unknown went wrong
			response.status = 500
			return {"info":str(e)}
	finally:
		if "db" in locals(): db.close()

