import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
 
mapeamento = [
    ('/', FraseDoDia)
]
app = webapp2.WSGIApplication(mapeamento)
run_wsgi_app(app)
