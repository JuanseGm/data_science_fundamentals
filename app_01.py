# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:36:23 2020

@author: JuanseGm
"""

from flask import Flask
from flask import jsonify
import csv

filename = 'iris.csv'
raw_data = open(filename, 'r')
reader = csv.reader(raw_data, delimiter = ',', quoting = csv.QUOTE_NONE)
x = list(reader)

app = Flask (__name__)

@app.route('/json_from_list')
def show_list():
    return jsonify(x)

if __name__ == '__main__':
    app.run()

