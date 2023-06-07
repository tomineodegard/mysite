from bottle import get, template, request
import x


@get("/deactivate_user/<user_deactivate_key>")
def _(user_deactivate_key):
    try:
        db = x.db()

        user = db.execute("SELECT * FROM users WHERE user_deactivate_key = ?", (user_deactivate_key,)).fetchone()
        print("user: " +"-"*50)
        print(user)

        print("user_deactivate_key: " +"-"*50)
        print(user_deactivate_key)

        total_changes = db.execute("UPDATE users SET user_deactivate_key = ? AND user_is_active = ?",("", 0)).rowcount
        if not total_changes: raise Exception (400, "user is not deactivated, something went wrong")
        print("total_changes: " +"-"*50)
        print(total_changes)

        # TO DO: Delete cookie and redirect to indexpage
        db.commit()
        return template("confirm_deactivate_account", title="Deactivate user - Twitter", user_deactivate_key=user_deactivate_key, user=user)
    except Exception as ex:
        if "db" in locals(): db.rollback()
        print("Exection: " +"-"*50)
        print(ex)
        return f"{str(ex)}"

    finally:
        if "db" in locals():
            db.close()