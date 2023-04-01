from program import app
from flask import render_template
from markupsafe import escape
from flask import request
import pprint

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/100Days')
def p100Days():
    return render_template("100Days.html")


@app.get("/hello/<user>")
def hello(user=None):
    return render_template("hello.html", user=escape(user))


@app.get("/form")
def form():
    return render_template("form.html")

@app.route("/post", methods=["GET", "POST"])
def post():
    pprint.pprint(request.form)
    return escape(request.form["username"])