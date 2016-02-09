#!/usr/bin/env python
#coding: utf-8

from flask import Flask
from flask.ext.basicauth import BasicAuth
from flask_pybankid import PyBankID
import os

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.getenv('USR')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('PASS')
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)

app.config.from_object('server.config')
bankid = PyBankID(app)
