from bottle import post, request, response
import x
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid

@post("/api-request-deactivate-user-key")
def _():
    try:
        db = x.db()
        user_id = request.forms.get("user_id")
        user_deactivate_key = str(uuid.uuid4()).replace("-","")
        user_email = db.execute("SELECT user_email FROM users WHERE user_id=?", (user_id,)).fetchone()
        username = db.execute("SELECT username FROM users WHERE user_id=?", (user_id,)).fetchone()

        # print("user email:"+"-"*50)
        # print(user_email["user_email"])

        # print("user_deactivate_key:"+"-"*50)
        # print(user_deactivate_key)

        total_changes = db.execute(f"""
            UPDATE users
            SET user_deactivate_key = ?
            WHERE user_id = ?
        """, (user_deactivate_key, user_id)).rowcount
        if not total_changes: raise Exception(400, "Something went wrong")


        sender_email = "tomineodegard99@gmail.com"
        receiver_email = "tomineodegard99@gmail.com"
        app_password = "ufouvebjcndaumua"
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Deactivate user"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = f"""\
		Hi {username}.
		Follow the link below to confirm the deactivation of your account with the username {username}.
        Your deactivate key is: {user_deactivate_key}.
        Click <a href="http://127.0.0.1:4005/deactivate_user/{user_deactivate_key}">here</a> to complete the deactivation.
		"""

        html = f"""\
		<html>
		<body>
			<p>Hi {username}.<br>Follow the link below to confirm the deactivation of your account with the username {username}.<br>Your deactivate key is: {user_deactivate_key}.<br>Click <a href="http://127.0.0.1:4005/deactivate_user/{user_deactivate_key}">here</a> to complete the deactivation.
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
        "info": f"user with id: {user_id} has requested to deactivate there account. Email is sent to {user_email}",
        "user_deactivate_key": user_deactivate_key,
    }
    except Exception as ex:
        print("-"*30)
        print(ex)
        response.status = 400
        return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()







