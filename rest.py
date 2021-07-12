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

dir_local_img_default = '/home/flask-restfull/'

app = Flask(__name__, template_folder='templates')
api = Api(app, version='1.0', title='API exercise-data-engineer',
    description='API exercise-data-engineer',
)


@api.route('/finishADF')
class finishADF(Resource):
    def put(self):

        time_start = datetime.now() 

        print('hola')

        subprocess.call(['/home/echo.sh'],shell=True)

        return {'Result':'Ok'}



  

if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.debug = True
    app.run(host='0.0.0.0', port=5000)



