import os

import folium
from folium import plugins

import pandas as pd

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

todos = []

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

folium_parameters = { 'location': [34.6937, 135.5023], 'zoom_start' : 5, 'width': 1200, 'height': 1200 }
folium_map = folium.Map(**folium_parameters)

@app.route("/", methods = ["GET"])
def choose_std():
    return render_template("standard.html")

@app.route("/year", methods = ["GET", "POST"])
def template():
    if request.method == "GET":
        return render_template("tourism.html")
    else:
        tyear = request.form.get("year")
        print(tyear)

    tourist_data = pd.read_csv("Visit Rate Ranking.csv")
    tourist_data = tourist_data.dropna()
    tourist_data.head()

    return render_template("my_map.html")

@app.route("/request", methods=["GET", "POST"])
def moreinfo():
    if request.method == "GET":
        return render_template("request.html",todos = todos)
    else:
        comment = request.form.get("comment")
        todos.append(comment)
        return render_template("request.html")