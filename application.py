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

# from helpers import trackpop

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

list = []

# db = SQL("TODO")

folium_map = folium.Map(location = [34.6937, 135.5023], zoom_start = 7, tiles="CartoDB dark_matter")

@app.route("/", methods = ["GET"])
def choose_std():
    return render_template("standard.html")

@app.route("/year")
def template():
    return render_template("tourism.html")

def initialmap():
    # folium.Marker(
    # location=[35.6762, 139.6503],
    # popup='Osaka',
    # icon=folium.Icon(color='red', icon='info-sign')
    # ).add_to(folium_map)

    tourist_data = pd.read_csv("Visit Rate Ranking.csv")
    tourist_data = tourist_data.dropna()
    tourist_data.head()

    for index, row in tourist_data.iterrows():
        folium.CircleMarker(
            location=[float(row['Longitude']), float(row['Latitude'])],
            popup=row['Prefecture'],
            radius=3*row['2017'],
            color='#3186cc',
            fill=True,
            fill_color='#3186cc').add_to(folium_map)

    folium_map.save("templates/my_map.html")
    return render_template("my_map.html")

@app.route("/request", methods=["GET", "POST"])
def moreinfo():
    if request.method == "GET":
        return render_template("request.html")
    else:
        comment = request.form.get("comment")
        if not comment:
            return redirect("/")
        list.append(comment)
        return render_template("request.html",comment = comment)

        # maybe we could add the comment to the upcoming list under comments and people can like/hate it depending on what