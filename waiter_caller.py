#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:49:48 2018

@author: bilal
"""


from flask import Flask

app = Flask(__name__)



@app.route("/")
def home():
    return "Site under construction"




if __name__ == '__main__':
    app.run(debug=True)
    
    