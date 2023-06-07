from bottle import post, request
import x
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid


@post("/api-forgot-password")
def _():
    try:
        
        username = request.forms.get("username")
        user_email = request.forms.get("user_email")

        db = x.db()
        verify_identity = db.execute("SELECT * FROM users WHERE username = ? AND user_email = ?", (username, user_email)).fetchone()
        if not verify_identity: raise Exception ("Something went wrong. Please doublecheck the information you have entered.")


        user_reset_password_key = str(uuid.uuid4()).replace("-","")

        total_changes = db.execute("""
            UPDATE users
            SET user_reset_password_key = ?
            WHERE user_email = ? AND username = ?
        """, (user_reset_password_key, user_email, username)).rowcount

        if not total_changes: raise Exception(400, "Could not update user_reset_password_key.")


        sender_email = "tomineodegard99@gmail.com"
        receiver_email = "tomineodegard99@gmail.com"
        app_password = "ufouvebjcndaumua"
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Reset password"
        message["From"] = sender_email
        message["To"] = receiver_email
        
        text = f"""\
		Hi {username}.
		Looks like you have forgotten the password. Lets help you get access to your account again by resetting your password. Click the link below to reset your password.
        Your reset key is: {user_reset_password_key}.
		http://127.0.0.1:4321/reset_password/{user_reset_password_key}"""

        html = f"""\
		<html>
            <body>
                <p>Hi {username}.<br>Looks like you have forgotten the password. Lets help you get access to your account again by resetting your password.</p>
                <button class=`ml-auto px-4 py-2 text-black text-base font-medium bg-white rounded-full`>Click <a href="http://127.0.0.1:4321/reset_password/{user_reset_password_key}">here </a>to reset password.</button>
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

        return {"info":"An email is sent, please check your inbox to reset your password."}
    except Exception as e:
        print(e)
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
