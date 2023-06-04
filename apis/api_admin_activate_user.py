from bottle import post, request, response
import x
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl

@post("/api-admin-activate-user")
def _():
    try:
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        if not cookie_user["user_is_active"] == 2 or not cookie_user: return {"info": "no access"}

        user_id = request.forms.get("user_id")

        db = x.db()
        user = db.execute("SELECT * FROM users where user_id = ?",(user_id,)).fetchone()
        username = user["username"] 
        total_changes = db.execute(f"""
            UPDATE users
            SET user_is_active = 1
            WHERE user_id=?
        """, (user_id,)).rowcount
        if not total_changes: raise Exception(400, "user not found")

        sender_email = "tomineodegard99@gmail.com"
        receiver_email = "tomineodegard99@gmail.com"
        app_password = "ufouvebjcndaumua"
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "User activated"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = f"""\
		Hi @{username}.
		Your account has been activated again, and you can use your Twitter as previously.
		"""

        html = f"""\
		<html>
		<body>
			<p>Hi @{username}.<br>Your account has been activated again, and you can use your Twitter as previously.
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

        return {"info":"ok"}
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback()
        try: # Controlled exception, usually comming from the x file
            response.status = e.args[0]
            return {"info":e.args[1]}
        except: # Something unknown went wrong
            # unknown scenario
            response.status = 500
            return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()