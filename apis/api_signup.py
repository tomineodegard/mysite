from bottle import post, response, request
import x
import uuid
import time
import bcrypt
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

##############################
@post("/api-signup")
def _():
	try:
		db = x.db()
		taken_username = db.execute("SELECT username FROM users WHERE username = ?",(request.forms.username,)).fetchone()
		
		print(taken_username)
		
		username = x.validate_username(taken_username)

		user_firstname = x.validate_user_firstname()
		user_lastname = x.validate_user_lastname()
		user_email = x.validate_user_email()
		user_password = x.validate_user_password()
		salt = bcrypt.gensalt()
		user_id = str(uuid.uuid4().hex)
		activation_key = str(uuid.uuid4().hex)
		user_reset_password_key = str(uuid.uuid4().hex)
		# user_deactivate_key = str(uuid.uuid4().hex)

		new_user = {
            "user_id" : user_id,
            "username" : username,
            "user_email" : user_email,            
            "user_password": bcrypt.hashpw(user_password.encode('utf-8'), salt),
            "user_created_at" : int(time.time()),
            "user_firstname" : user_firstname,
            "user_lastname" : user_lastname,
	   		"user_bio" : "",
            "user_is_verified" : 0,
            "user_total_followers" : 0,
            "user_total_following" : 0,
            "user_total_tweets" : 0,
            "user_profile_picture" : "",
	        "user_cover_picture" : "",
			"user_is_activated" : 0,
			"user_is_active" : 1,
			"user_activation_key" : activation_key,
			"user_reset_password_key":user_reset_password_key,
			"user_deactivate_key":""
        }
		
		# insert values from the 'new user dictionary' f-stringing the keys
		values = ""
		for key in new_user:
			values += f":{key},"
		# right-strip the values inserted to remove potential spaces
		values = values.rstrip(",")
		print(values)

		# Connect to database	
		
		total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", new_user).rowcount        
		if total_rows_inserted != 1: raise Exception("Please, try again")

		# Send verification email to new user
		sender_email = "tomineodegard99@gmail.com"
		receiver_email = "tomineodegard99@gmail.com"
		# receiver_email = user_email
		app_password = "ufouvebjcndaumua"


		message = MIMEMultipart("alternative")
		message["Subject"] = "Verification email"
		message["From"] = sender_email
		message["To"] = receiver_email

		text = """\
		Hi {user_firstname} {user_lastname}.
		Thank you for signing up to Twitter, with the username {username}.
		Now there is one last step for you to complete, before you can log in to your account.
		Please click this link to activate your account.
		http://127.0.0.1:4321/activate_user/{activation_key}"""
		html = f"""\
		<html>
		<body>
			<p>Hi {user_firstname} {user_lastname}.<br>
			Thank you for signing up to Twitter, with the username {username}.<br>
			Now there is one last step for you to complete, before you can log in to your account.<br>
			Please click this link to activate your account.<br>
			Click <a href="http://127.0.0.1:4321/activate_user/{activation_key}">here</a>.
			</p>
		</body>
		</html>
		"""

		part1 = MIMEText(text, "plain")
		part2 = MIMEText(html, "html")

		message.attach(part1)
		message.attach(part2)

		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(sender_email, app_password)
			server.sendmail(
				sender_email, receiver_email, message.as_string()
			)

		db.commit()
		return {
			"info" : "a new user is created", 
			"user_id" : user_id,
			"username" : username
		}
	except Exception as ex:
		print("-"*30)
		print(ex)
		try: # Controlled exception, usually comming from the x file
			response.status = ex.args[0]
			return {"info":ex.args[1]}
		except: # Something unknown went wrong
			if "user_email" in str(ex): 
				response.status = 400 
				return {"info":f"{ex}"}

			if "username" in str(ex): 
				response.status = 400 
				print(ex)
				return {"info":f"{ex}"}

			# unknown scenario
			response.status = 500
			return {"info":str(ex)}
	finally:
		if "db" in locals(): db.close()

