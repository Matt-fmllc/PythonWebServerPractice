"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
#from Character import HelloWorld
#import Character_Facade

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps

from flask import Flask
app = Flask(__name__)
#CharacterApi = Api(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

import Character_Facade
from Character_Facade import *


# @app.route('/')
# def hello():
#    """Renders a sample page."""
#    return "Hello World!"

#class HelloWorld(Resource):
#    def get(self):
#        return "My Hello World!"
#
#CharacterApi.add_resource(HelloWorld,'/', '/Hello')

    

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
