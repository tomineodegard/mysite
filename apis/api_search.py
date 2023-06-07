from bottle import post, request, response
import json
import x

@post("/api-search")
def _():
    try:
        cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)
        username = cookie_user["username"]

        # Get the search query from the JSON payload
        search_input = request.json["search_input"]
        print(search_input)


        
        db = x.db()
        results = db.execute("SELECT * FROM users WHERE username LIKE ? AND username != ?", ('%' + search_input + '%', username,)).fetchall()

        # Convert the rows to a list of dictionaries
        users = []
        for row in results:
            user = {
                "user_id": row["user_id"],
                "user_email": row["user_email"],
                "username":row["username"],
                "user_profile_picture":row["user_profile_picture"]
            }
            users.append(user)

        # Return the list of users as JSON
        response.set_header("content-type", "application/json")
        print(type(users))
        if not search_input:
            return json.dumps([])
        return json.dumps(users)

    except Exception as e:
        print(e)

    finally:
        db.close()