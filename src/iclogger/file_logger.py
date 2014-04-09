# -*- coding: utf-8 -*-
'''
Created on 2014-04-09

This logger saves the information into file system.

@author: Krzysztof Langner
'''
import datetime
import json
import os
from flask import Flask
from flask import request
from iclogger.settings import FILE_STORAGE

app = Flask(__name__)

@app.route("/")
def log():
    content_id = request.args.get("content", "")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = FILE_STORAGE + content_id + "/" + today + ".log" 
    try:
        log_file = open(filename, 'a+')
    except IOError:
        os.makedirs(FILE_STORAGE + content_id)
        log_file = open(filename, 'a+')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    data = {'time':timestamp}
    for key in request.args:
        if key != 'content':
            data[key] = request.args.get(key, "") 
    log_file.write(json.dumps(data) + "\n")
    log_file.close()
    return ""
