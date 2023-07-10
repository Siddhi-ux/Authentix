# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 13:14:33 2023

@author: SIDDHI MANGALAM
"""

from flask import Flask as f
import pandas as pd
import numpy as np
import pickle

app=f(__name__)
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Siddhi Manglam"

if __name__ =="__main__":
    app.run()