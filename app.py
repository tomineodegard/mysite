# 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

#https://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@github.com/tomineodegard/mysite.git

from bottle import default_app, get, post, run
import git
 
@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./mysite')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""
 
 
##############################
@get("/")
def _():
  return "Two"
 
##############################
try:
  import production
  application = default_app()
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=80, debug=True, reloader=True)