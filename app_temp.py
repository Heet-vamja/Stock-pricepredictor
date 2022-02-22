from flask import Flask, render_template, request
import yfinance as yf

import pandas as pd
import numpy as np
import pandas_datareader as web

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from datetime import date, datetime, timedelta
from keras.models import load_model
import math

app_temp = Flask(__name__)

@app_temp.route('/')
def man():
    return render_template('home.html')

@app_temp.route('/predict', methods=['POST'])
def home():
    data = request.form['stock_name']
    return render_template('after.html')
    
if __name__ == "__main__":
    app_temp.run(debug=False)
    
