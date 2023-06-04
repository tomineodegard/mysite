from bottle import get, template, request, response
import x
import traceback

@get("/adminpanel")
def _():
	try:
		db = x.db()
		cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
		user_id = cookie_user["user_id"]
		# username = cookie_user["username"]

		if cookie_user:
			users = db.execute("SELECT * FROM users WHERE NOT user_id = ? ORDER BY username ASC",(user_id,)).fetchall()
		else: users = None   
	
		db.commit()
		return template("adminpanel", title="Admin page - Twitter", cookie_user=cookie_user, users=users)
	except Exception as ex:
		print("-"*30)
		print(ex)
		if "db" in locals(): db.rollback()
		response.status = 400
		traceback.print_exc()
		return {"info":str(ex)}
	finally:
		if "db" in locals(): db.close()
