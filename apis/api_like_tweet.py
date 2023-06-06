# from bottle import post, request, response
# import x

# @post("/api-like-tweet")
# def _():
#     try:
#         cookie_user = request.get_cookie("cookie_user", secret=x.COOKIE_SECRET)

#         if cookie_user:
#             user_id = cookie_user["user_id"]
#         tweet_id = request.forms.get("tweet_id", "")

#         db = x.db()
#         total_changes = db.execute("INSERT INTO likes(like_user_fk, like_post_fk) VALUES(?,?)", (user_id, tweet_id))
#         if not total_changes: raise Exception(400, "user not found")
        
#         db.commit()
#         return {"info":"ok"}
#     except Exception as e:
#         print(e)
#         if "db" in locals(): db.rollback()
#         try: # Controlled exception, usually comming from the x file
#             response.status = e.args[0]
#             return {"info":e.args[1]}
#         except: # Something unknown went wrong
#             if "users.user_email" in str(e):
#                 response.status = 400
#                 return {"info":"user_email already exists"}
#             # unknown exception
#             response.status = 500
#             return {"info":str(e)}
#     finally:
#         if "db" in locals(): db.close()