from bottle import post, request, response

@post("/api-follow")
def _():
    try:
        # TODO: get user from cookie
        # user = request.get_cookie("user", secret="xxxxxx")
        cookie_user = request.get_cookie("cookie_user", secret="my-secret")

        # TODO: get user id from the user from the cookie
        # TODO: validate the followeer's id
        # TODO: connect to the database
        # TODO: insert into followers table
        user_followee_fk = request.forms.get("user_followee_fk", "")
        return {"info":f"following user with id {user_followee_fk} successful"}
    except Exception as e:
        print(e)
        pass
    finally:
        pass
