from bottle import get, response

@get("/logout")
def _():
  response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
  response.add_header("Pragma", "no-cache")
  response.add_header("Expires", 0)    
  response.delete_cookie("cookie_user")
  response.status = 303
  response.set_header("Location", "/")
  return