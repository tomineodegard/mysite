from bottle import post

@post("/activate_user")
def _():
    try:
        return {"info":"ok"}
    except Exception as ex:
        print(ex)
        pass
    finally:
        pass