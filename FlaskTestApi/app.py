"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

import ctest

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
# wsgi_app = app.wsgi_app

class test(Resource):
    def get(self):
        return ctest.result()

api.add_resource(test, '/test')

#@app.route('/')
#def hello():
#    """Renders a sample page."""
#    return "Hello World!"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)


