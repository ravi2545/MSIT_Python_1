from django.shortcuts import redirect
from flask import Flask, render_template, request, url_for, flash
from Databaseconn import *
import re
import json
app = Flask(__name__)


@app.route('/')
def home():
    return  render_template("homepage.html")

@app.route('/uregister')
def uregister():
    return render_template("uregister.html")

@app.route('/ulogin')
def ulogin():
    return render_template("ulogin.html")

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method=='POST':
        email = request.form['email']
        psw = request.form['psw']
        pswrepeat = request.form['pswrepeat']
        if psw==pswrepeat:
            if len(psw)>=6 and re.search("[A-Za-z0-9@]",psw):
                ob = Databases()
                ob.db_connect(email,psw)
    return render_template("homepage.html")



@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method=='POST':
        username = request.form['uname']
        password = request.form['psw']
        obj = Databases()
        result = obj.fetch(username, password)
        return result

@app.route('/kalyan')
def kalyan():
    obj = Databases()
    r = obj.Raw_data()
    return json.dumps(r)

    # @app.route('/hom/<name>')
# def home(name):
#     return "Welcom {}".format(name)

if __name__ == "__main__":
    app.run(debug=True)
