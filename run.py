#!/usr/bin/env python
#coding: utf-8

from server import app
print("Running server on http://localhost:5000")
app.run(host='0.0.0.0', debug=True)
