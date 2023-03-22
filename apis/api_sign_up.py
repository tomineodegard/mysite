from bottle import post, request, response
import x
@post("/api-sign-up")
def _():
    try:
        username = x.validate_username()
        user_id = 1
        user = {
            "user_id" : user_id,
            "username" : username
        }
        values = ""
        for key in user:
            values = values + f":{key},"
            values = values.rstrip(",")
            print("-"*50)
            print(values)
            db.execute(f"INSERT INTO users VALUES({values})", user)
        return "ok"
    
    except Exception as e:
        print(e)
        return {"info":str(e)}
    
    finally:
        if db in locals(): db.close()



