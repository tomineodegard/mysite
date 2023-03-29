from bottle import post, response
import x
import uuid
import time
import bcrypt

##############################
@post("/api-signup")
def _():
	try:
		# Validate the information inserted by the user
		username = x.validate_username()
		user_email = x.validate_user_email()
		user_password = x.validate_user_password()
		
		# Adding the salt to password
		salt = bcrypt.gensalt()
		user_id = str(uuid.uuid4().hex)
		
        # New user dictionary
		new_user = {
            "user_id" : user_id,
            "username" : username,
            "user_email" : user_email,            
            "user_password": bcrypt.hashpw(user_password.encode('utf-8'), salt),
            "user_created_at" : int(time.time()),
            "user_firstname" : "",
            "user_lastname" : "",
            "user_verified" : 0,
            "user_total_followers" : 0,
            "user_total_following" : 0,
            "user_total_tweets" : 0,
            "user_profile_picture" : "",
	        "user_cover_picture" : ""
        }
		
		# create placed holders for values
		values = ""
		for key in new_user:
			values += f":{key},"
		# right strip the values inserted to remove potential spaces
		values = values.rstrip(",")
		print(values)	
		db = x.db()
		total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", new_user).rowcount        
		if total_rows_inserted != 1: raise Exception("Please, try again")
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
				return {"info":"user_email already exists"}
			if "username" in str(ex): 
				response.status = 400 
				return {"info":"username already exists"}
			# unknown scenario
			response.status = 500
			return {"info":str(ex)}
	finally:
		if "db" in locals(): db.close()

