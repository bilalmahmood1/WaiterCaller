
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:49:48 2018

@author: bilal
"""

from flask import Flask
from flask import render_template
from flask.ext.login import LoginManager
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.ext.login import logout_user
from flask.ext.login import  current_user
from flask import redirect
from flask import url_for
from flask import request

from mockdbhelper import MockDBHelper as DBHelper
from user import User
import config
from passwordhelper import PasswordHelper as PHelper
from helper import HelperLibrary 

from bitlyhelper import BitlyHelper

import datetime

app = Flask(__name__)
app.secret_key = 'ae+4YjO+l+GMTjsMPu+JNpFb4g55YbGgGSfIBt57mNWbiB/PF7kNGQQ4KCqiCkSrCAmVGMvku00GuJoMkFV3xTaAGA+5/f4Bqye'
login_manager = LoginManager()
login_manager.init_app(app)

DB = DBHelper()
PH = PHelper()
H = HelperLibrary()
BH = BitlyHelper()

## Target response time to resolve the request
TARGET_RESPONSE = 300


@login_manager.user_loader
def load_user(user_id):
	user_password = DB.get_user(user_id)
	if user_password:
		return User(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return render_template("unauthorized.html")



@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard")
@login_required
def dashboard():
    now = datetime.datetime.now()
    requests = DB.get_requests(current_user.get_id())
    for req in requests:
        deltaseconds = (now - req['datetime']).seconds
        req['wait_minutes'] = "{} minutes {} seconds".format((deltaseconds//60), str(deltaseconds % 60).zfill(2))
        req['time_elapsed'] = min(int(100 * deltaseconds/TARGET_RESPONSE), 100)
    return render_template("dashboard.html",
    					   user = current_user.get_id(),
                        calls = len(requests),
                        requests = requests)

@app.route("/account")
@login_required
def account():
    return render_template("account.html",
                           user = current_user.get_id(),
                           table = DB.get_tables(current_user.get_id()))



@app.route("/login", methods=['POST'])
def login():
    email = request.form.get("email")
    entered_password = request.form.get("password")
    user_credentials = DB.get_user(email)
    
    if user_credentials:
        hashed = user_credentials["hashed"]
        salt = user_credentials["salt"]
        if PH.validate_password(entered_password, salt, hashed):
            user = User(email)
            login_user(user)        
            return redirect(url_for('dashboard'))
        ## Incorrect password
        else:
            return redirect(url_for('home'))
    ## Please register
    else:
        return redirect(url_for('home'))


@app.route("/register", methods=['POST'])
def register():
    email = request.form.get("email")
    password1 = request.form.get("password")
    password2 = request.form.get("password2")
    
    if DB.get_user(email):
        return redirect(url_for('home'))
     
    if password1 != password2:        
        return redirect(url_for('home'))
     
    salt = PH.get_salt()
    hashed = PH.get_hash(password1 + salt)
    DB.add_user(email, salt, hashed)
     
    return redirect(url_for('home'))

     
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/account/createtable", methods=["POST"])
@login_required
def account_createtable():
    tablename = request.form.get("tablenumber")
    tableid = DB.add_table(tablename, current_user.get_id())
    new_url = config.base_url + "newrequest/" + str(tableid)
    DB.update_table(tableid, BH.shorten_url(new_url))
    return redirect(url_for('account'))

@app.route("/account/deletetable")
@login_required
def account_deletetable():
    tableid = int(request.args.get("tableid"))
    DB.delete_table(tableid)
    return redirect(url_for('account'))



@app.route("/dashboard/resolve")
@login_required
def dashboard_resolve():
    requestid = int(request.args.get("request_id"))
    DB.delete_request(requestid)
    return redirect(url_for('dashboard'))


@app.route('/newrequest/<tid>')
def newrequest(tid):
    table_id = int(tid)
    table = DB.get_table_id(table_id)
    table_number = table["number"]
    table_owner = table["owner"]
    time = datetime.datetime.now()
    DB.add_request(table_id, time,table_number,table_owner)
    return render_template("newrequest.html",
                           table_number = table_number)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
    