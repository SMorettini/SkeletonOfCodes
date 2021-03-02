import os, shutil
import datetime
import logging
import json
import random
import pandas as pd
from math import sqrt


from flask import (
    abort,
    Blueprint,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
    Response,
    session,
    jsonify,
    send_file)

from uuid import uuid4
import sys
from werkzeug.utils import secure_filename

from flask import current_app as app
landing = Blueprint('landing', __name__)


prediction_table={}


df=pd.read_csv("data.csv")

@landing.route('/', methods=['GET'])
def index():
    return jsonify({"Message" : "Hello from the website :)"})

@landing.route('/update/test', methods = ['POST'])
def test():
    return jsonify({"TEST" : "Hi"})

@landing.route('/update/transaction', methods = ['POST'])
def new_transaction():
    content = request.get_json()

    data=request.get_json()
    #Simulate the online learnig
    for row in data:
        data1=row['data1']

        for p in row['items']:
            category = p["cat_id"]
            
    return jsonify(dictionary_data)

@landing.route('/get/suggestion')
def suggestion():
    data=request.args.get("data_label")
    timestamp=int(request.args.get("timestamp"))

    items=[]

    return jsonify({"Message" : "Wow", "items":items})

def util_function(a, b):
  return a + b
