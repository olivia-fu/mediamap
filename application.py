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

actualyear = 0

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

<<<<<<< HEAD
folium_parameters = { 'location': [34.6937, 135.5023], 'zoom_start' : 5, 'width': 1200, 'height': 1200 }
folium_map = folium.Map(**folium_parameters)
=======
folium_map = folium.Map(location= [34.6937, 135.5023], zoom_start= 7)
>>>>>>> d852fe0b9d9b376f9d161237ff381141dfa5ea3c

@app.route("/", methods = ["GET"])
def choose_std():
    return render_template("standard.html")

@app.route("/year", methods = ["GET", "POST"])
def template():
    if request.method == "GET":
        return render_template("tourism.html")
    else:
        tyear = request.form.get("year")
<<<<<<< HEAD
        print(tyear)
=======
        actualyear = tyear

        # if tyear == "2016":
        #     for index, row in tourist_data.iterrows():
        #         folium.CircleMarker(
        #             location=[float(row['Longitude']), float(row['Latitude'])],
        #             popup=row[tyear],
        #             radius=3*row[tyear],
        #             color='#cc3131',
        #             fill=True if while == "2016",
        #             fill_color='#cc3131').add_to(folium_map)
        #     folium_map.save("templates/my_map.html")
        #     return render_template("my_map.html")

        # if tyear == "2015":
        #     for index, row in tourist_data.iterrows():
        #         folium.CircleMarker(
        #             location=[float(row['Longitude']), float(row['Latitude'])],
        #             popup=row[tyear],
        #             radius=3*row[tyear],
        #             color='#31cc55',
        #             fill=True while tyear == "2015",
        #             fill_color='#31cc55').add_to(folium_map)
        #     folium_map.save("templates/my_map.html")
        #     return render_template("my_map.html")

        # if tyear == "2014":
        #     for index, row in tourist_data.iterrows():
        #         folium.CircleMarker(
        #             location=[float(row['Longitude']), float(row['Latitude'])],
        #             popup=row[tyear],
        #             radius=3*row[tyear],
        #             color='#cc31b5',
        #             fill=True while tyear == "2014",
        #             fill_color='#cc31b5').add_to(folium_map)
        #     folium_map.save("templates/my_map.html")
        # folium_map.save("templates/my_map.html")
        return render_template("my_map.html")
        #     return render_template("my_map.html")

@app.route("/map", methods = ["GET"])
def resultmap():
    film_data = pd.read_csv("film.csv")
    film_data = film_data.dropna()
    film_data.head()

    for index, row in film_data.iterrows():
        folium.Marker(
            location=[float(row['Longitude']),float(row['Latitude'])],
            popup = row['Film'],
            icon=folium.Icon(color='red', icon='info-sign')).add_to(folium_map)
>>>>>>> d852fe0b9d9b376f9d161237ff381141dfa5ea3c

    tourist_data = pd.read_csv("Visit Rate Ranking.csv")
    tourist_data = tourist_data.dropna()
    tourist_data.head()

    if actualyear == 2017:
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

    if actualyear == 2016:
        for index, row in tourist_data.iterrows():
            folium.CircleMarker(
                location=[float(row['Longitude']), float(row['Latitude'])],
                popup=row['Prefecture'],
                radius=3*row['2016'],
                color='#cc3131',
                fill=True,
                fill_color='#cc3131').add_to(folium_map)
        folium_map.save("templates/my_map.html")
        return render_template("my_map.html")


@app.route("/request", methods=["GET"])
def moreinfo():
    if request.method == "GET":
        return render_template("request.html",todos = todos)
    else:
        todo = request.form.get("comment")
        print(todo)
        todos.append(todo)
        return render_template("request.html")
