#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:49:48 2018

@author: bilal
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(port = 5001, debug=True)
    
    