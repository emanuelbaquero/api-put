import json, subprocess, random, time,os,io
from flask import Flask, request
from flask_restplus import Api, Resource, fields, reqparse, inputs
from flask import Flask, render_template
from flask import make_response, request, Response
from flask import jsonify
from json import JSONEncoder
import pandas as pd
from datetime import datetime
from werkzeug.middleware.proxy_fix import ProxyFix
import subprocess
import pandasql as ps
import boto3
import pymongo
from pymongo import MongoClient
from flask import Flask, Response

import uuid
from datetime import datetime, timedelta


from flask_restful import reqparse
parser = reqparse.RequestParser()

dir_local_img_default = '/home/flask-restfull/'

app = Flask(__name__, template_folder='templates')
api = Api(app, version='1.0', title='API exercise-data-engineer',
    description='API exercise-data-engineer',
)





@api.route('/requests')
class post_create_record(Resource):
    def post(self):
        """Create a User request record
        @param username: post : the requesters for the username 
        @param password: post : the title of the password
        @return token:: a new_uuid as a flask/response object \
        with application/json mimetype.
        @raise 400: misunderstood request
        """
        if not request.get_json():
            return Response(status=400)
        data = request.get_json()
        print(data)


        if not data.get('username'):
            return Response(status=400)
        if not data.get('password'):
            return Response(status=400)

        new_uuid = str(uuid.uuid4())
        print(new_uuid)

        user_request = {
            'username': data['username'],
            'password': data['password'],
            'timestamp': datetime.now().timestamp()
        }
        print(user_request)
        #USER_REQUESTS[new_uuid] = user_request
        #HTTP 201 Created
        return jsonify({"token": new_uuid, 'data':user_request})



@api.route('/finishADF')
class post_create_record(Resource):
    def post(self):

        subprocess.run(['echo','Hola Mundo!', '>','/home/holaMundo.txt'])

        return jsonify({"Result": 'Ok'})

        


  

if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.debug = True
    app.run(host='0.0.0.0', port=5000)



