from flask import Flask, url_for
from flask import request
from flask import json
from flask import Response
from pymongo import MongoClient
import os
import json
import numpy as np
import pandas as pd
import cPickle as pickle
import predict

os.chdir('/Users/kellypeng/Desktop/dsi-fraud_detection_case_study')

app = Flask(__name__)

@app.route('/')
def api_root():
    ls = collection.find_one()
    return ls

@app.route('/score', methods = ['GET', 'POST'])
def api_articles():
        if request.method == 'POST':
            data, raw_file = predict.get_data('files/example.json')
            # df_feature_engineered = predict.feature_engineering(data)
            # probability = predict.predict(df_feature_engineered, model)
            # predict.create_json(raw_file,probability,collection)
            return raw_file
        if request.method =='GET':
            data, raw_file = predict.get_data('files/example.json')
            # df_feature_engineered = predict.feature_engineering(data)
            # probability = predict.predict(df_feature_engineered, model)
            # predict.create_json(raw_file,probability,collection)
            return raw_file

# @app.route('/articles/<articleid>')
# def api_article(articleid):
#     return 'You are reading ' + articleid

# @app.route('/hello')
# def api_hello():
#     if 'name' in request.args:
#         return 'Hello ' + request.args['name']
#     else:
#         return 'Hello John Doe'
#
#
# @app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
# def api_echo():
#     if request.method == 'GET':
#         return "ECHO: GET\n"
#
#     elif request.method == 'POST':
#         return "ECHO: POST\n"
#
#     elif request.method == 'PATCH':
#         return "ECHO: PACTH\n"
#
#     elif request.method == 'PUT':
#         return "ECHO: PUT\n"
#
#     elif request.method == 'DELETE':
#         return "ECHO: DELETE"
#
# @app.route('/messages', methods = ['POST'])
# def api_message():
#
#     if request.headers['Content-Type'] == 'text/plain':
#         return "Text Message: " + request.data
#
#     elif request.headers['Content-Type'] == 'application/json':
#         return "JSON Message: " + json.dumps(request.json)
#
#     elif request.headers['Content-Type'] == 'application/octet-stream':
#         f = open('./binary', 'wb')
#         f.write(request.data)
#         f.close()
#         return "Binary message written!"
#
#     else:
#         return "415 Unsupported Media Type ;)"

# @app.route('/hello', methods = ['GET'])
# def api_hello():
#     data = {
#         'hello'  : 'world',
#         'number' : 3
#     }
#     js = json.dumps(data)
#
#     resp = Response(js, status=200, mimetype='application/json')
#     resp.headers['Link'] = 'http://luisrei.com'
#
#     return resp

if __name__ == '__main__':
    client = MongoClient()
    db = client.fraud_detection
    collection = db.collection
    with open('best_model.pkl') as f:
        model = pickle.load(f)
    app.run(host='127.0.0.1', port=5000)
