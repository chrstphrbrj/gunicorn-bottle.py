
# BOTTLE.PY
import bottle
from bottle import route, run


# Initialize app
my_app = bottle.default_app()


@route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    # No need to set the port; bottle.py defaults to 8080 , gunicorn defaults to 8000
    my_app.run(host='localhost', debug=True)
