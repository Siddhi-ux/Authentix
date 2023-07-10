# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 13:04:34 2023

@author: SIDDHI MANGALAM
"""
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome"

@app.route('/predict')
def predict_note_authentication():
    variance = float(request.args.get("variance"))
    skewness = float(request.args.get("skewness"))
    curtosis = float(request.args.get("curtosis"))
    entropy = float(request.args.get("entropy"))

    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return "Hello, the answer is " + str(prediction)

@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return "The predicted value is: " + str(list(prediction))

if __name__ == "__main__":
    app.run()


