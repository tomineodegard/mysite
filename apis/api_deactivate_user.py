from bottle import get, response, request
import x

##############################
@get("/api-deactivate-user/<user_deactivate_key>")
def _(user_deactivate_key):
    try:
        print("****Hello")
        db = x.db()

        print("user_deactivate_key:"+"*"*50)
        print(user_deactivate_key)



        total_changes = db.execute(f"""
            UPDATE users
            SET user_is_active = 0, user_deactivate_key = ""
            WHERE user_deactivate_key = ?
        """, (user_deactivate_key,)).rowcount
        if not total_changes: raise Exception(400, "user not found")
        db.commit()
  
        return {"info":"I am inside api-deactivate-user"}
    except Exception as ex:
        print("-"*30)
        print(ex)
        response.status = 400
        return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()






