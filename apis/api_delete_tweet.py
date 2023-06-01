from bottle import delete, request, response
import x

@delete("/api-delete-tweet")
def _():
    try:
        tweet_id = request.forms.get("tweet_id", "")
        print("tweet_id:"+"-"*30)
        print(tweet_id)
        if not tweet_id: raise Exception(400, "could not delete this tweet")
        

        db = x.db()
        total_changes = db.execute("DELETE FROM tweets WHERE tweet_id = ?", (tweet_id,)).rowcount
        if total_changes != 1: raise Exception(400, "Error")
        db.commit()

        return {
            "info": f"tweet with id: {tweet_id} is deleted",
            "tweet_id": tweet_id 
                }
    except Exception as ex:
        print(ex)
        if "db" in locals(): db.rollback()
        try: # Controlled exception, usually comming from the x file
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except: # Something unknown went wrong
            # unknown exception
            response.status = 500
            return {"info":str(ex)}
    finally:
        db.close()