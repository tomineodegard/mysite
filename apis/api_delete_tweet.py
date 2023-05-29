from bottle import delete, request, response
import x

@delete("/api-delete-tweet")
def _():
    try:
        return {
            "info": "ok"
        }
    except Exception as ex:
        print("-"*30)
        print(ex)
        response.status = 400
        return {"info":str(ex)}
    finally:
        pass