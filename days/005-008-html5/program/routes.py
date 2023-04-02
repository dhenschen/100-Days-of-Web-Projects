from program import app
from flask import render_template
from markupsafe import escape
from flask import request
import pprint

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/signup', methods=["GET", "POST"])
def signup():
    pprint.pprint(request.form)
    return render_template("signup.html")