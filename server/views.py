#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from server import app

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    print("Running server on http://localhost:5000")
    app.run(host='0.0.0.0', debug=True)
