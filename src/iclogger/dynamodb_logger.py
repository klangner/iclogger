# -*- coding: utf-8 -*-
'''
Created on 2014-04-09

This logger saves the information into Amazon DynamoDB datastore.

@author: Krzysztof Langner
'''
import datetime
from flask import Flask
from flask import request
from iclogger.example_settings import TABLE_NAME
from boto.dynamodb2.table import Table

app = Flask(__name__)

@app.route("/")
def log():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    data = {'created_at':timestamp}
    for key in request.args:
        data[key] = request.args.get(key, "")
    table = Table(TABLE_NAME)
    table.put_item(data)
    return ""
