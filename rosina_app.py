import os
from flask import Flask, render_template
import requests
import json
import predict as pr
import pandas as pd
import cPickle as pickle
from pymongo import MongoClient

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route("/predict")
def get_data():
    req = requests.get('http://galvanize-case-study-on-fraud.herokuapp.com/data_point').content
    data = json.loads(req)

    cols = ['org_twitter','body_length','user_age','sale_duration2','delivery_method',
            'org_facebook','previous_payouts','has_analytics','venue_state',
            'org_desc', 'name']
    df_data = []
    for c in cols:
        df_data.append(data[c])

    df = pd.DataFrame([df_data],columns=cols)

    X = pr.feature_engineering(df)
    predict_proba = model.predict_proba(X)
    to_print = "The probability of this event being fraud is {}".format(str(predict_proba[:,1][0]))
    pr.send_to_db(data, predict_proba[:,1][0], collection)
    return to_print

# Homepage
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/summary')
def dash():
    preds = list(collection.find({},  {'probability':1, 'name':1, '_id':0}))
    for element in preds:
        element['probability'] = round(element['probability'],2)
        if element['probability'] > 0.2:
            element['fraud'] = 'High Risk'
        else:
            element['fraud'] = 'Low Risk'
    return render_template('table.html', preds=preds)

if __name__ == "__main__":

    with open('best_model_0816_2.pkl') as f:
        model = pickle.load(f)
    client = MongoClient()
    db = client.new_db
    collection = db.new_test
    app.run(port=5000, debug=True)
