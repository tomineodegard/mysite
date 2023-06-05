from bottle import delete, request, response
import x

@delete("/api-admin-delete-user")
def _():
    try:
        user_id = request.forms.get("user_id", "")
        if not user_id: raise Exception(400, "Could not delete user")
        print(user_id)

        db = x.db()
        total_changes = db.execute("DELETE FROM users WHERE user_id=?", (user_id,)).rowcount
        if not total_changes: raise Exception(400, "user not found")
        db.commit()

        return {"info":"ok", 
                "user_id":user_id
                }
    
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