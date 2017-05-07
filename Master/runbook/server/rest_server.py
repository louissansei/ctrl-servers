#! /usr/bin/env python3

from flask import Flask, request
from flask_restful import Resource, Api

from . import ssh_interface
from . import store_interface
from .. import config
from .utils import require_json

app = Flask(__name__)

api = Api(app)

class Run(Resource):
    @require_json
    def post(self):
       payload = request.get_json()
       body, return_code = ssh_interface.run(payload)
       return body, return_code

api.add_resource(Run, '/api/run')

class Configure(Resource):
    @require_json
    def post(self):
        payload = request.get_json()
        body, return_code = store_interface.configure(payload)
        return body, return_code

api.add_resource(Configure, '/api/configure')

def start():
    app.run(host=config.LISTEN_ON, port=config.PORT)
