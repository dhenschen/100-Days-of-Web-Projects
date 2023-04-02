from program import app
from flask import render_template, request
from markupsafe import escape
import pprint

from datetime import datetime
import requests


@app.route("/")
@app.route("/index")
def index():
    timenow = str(datetime.today())
    return render_template("index.html", time=timenow)


@app.route("/100Days")
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


@app.route("/chuck")
def chuck():
    joke = get_chuck_joke()
    return render_template("chuck.html", joke=joke)


def get_chuck_joke():
    r = requests.get("https://api.chucknorris.io/jokes/random")
    data = r.json()
    return escape(data["value"])


def get_number_trivia() -> (int, str):
    r = requests.get("http://numbersapi.com/random?json")
    r.raise_for_status()
    data = r.json()
    return data["number"], data["text"]


@app.route("/number")
def number():
    number, text = get_number_trivia()
    return render_template("number.html", number=escape(number), text=escape(text))


def get_poke_colors(color):
    r = requests.get("https://pokeapi.co/api/v2/pokemon-color/" + color.lower())
    pokedata = r.json()
    pokemon = []

    for i in pokedata["pokemon_species"]:
        pokemon.append(escape(i["name"]))

    return pokemon


@app.route("/pokemon", methods=["GET", "POST"])
def pokemon():
    pokemon = []
    if request.method == "POST" and "pokecolor" in request.form:
        color = request.form.get("pokecolor")
        pokemon = get_poke_colors(color)
    return render_template("pokemon.html", pokemon=pokemon)
