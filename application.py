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

folium_map = folium.Map(location= [34.6937, 135.5023], zoom_start= 7)

@app.route("/", methods = ["GET"])
def choose_std():
    return render_template("standard.html")

@app.route("/year", methods = ["GET", "POST"])
def template():
    if request.method == "GET":
        return render_template("tourism.html")
    else:
        tyear = request.form.get("year")
        actualyear = int(tyear)
        print(actualyear)
        return redirect("/map")

@app.route("/map2017", methods = ["GET"])
def resultmap2017():
    film_data = pd.read_csv("film.csv")
    film_data = film_data.dropna()
    film_data.head()

    for index, row in film_data.iterrows():
        folium.Marker(
            location=[float(row['Longitude']),float(row['Latitude'])],
            popup = row['Film'],
            icon=folium.Icon(color='red', icon='info-sign')).add_to(folium_map)

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

@app.route("/map2016", methods = ["GET"])
def resultmap2016():
    film_data = pd.read_csv("film.csv")
    film_data = film_data.dropna()
    film_data.head()

    for index, row in film_data.iterrows():
        folium.Marker(
            location=[float(row['Longitude']),float(row['Latitude'])],
            popup = row['Film'],
            icon=folium.Icon(color='red', icon='info-sign')).add_to(folium_map)

    tourist_data = pd.read_csv("Visit Rate Ranking.csv")
    tourist_data = tourist_data.dropna()
    tourist_data.head()

    for index, row in tourist_data.iterrows():
        folium.CircleMarker(
            location=[float(row['Longitude']), float(row['Latitude'])],
            popup=row['Prefecture'],
            radius=3*row['2016'],
            color='#3186cc',
            fill=True,
            fill_color='#3186cc').add_to(folium_map)
    folium_map.save("templates/my_map.html")
    return render_template("my_map.html")

@app.route("/map2015", methods = ["GET"])
def resultmap2015():
    film_data = pd.read_csv("film.csv")
    film_data = film_data.dropna()
    film_data.head()

    for index, row in film_data.iterrows():
        folium.Marker(
            location=[float(row['Longitude']),float(row['Latitude'])],
            popup = row['Film'],
            icon=folium.Icon(color='red', icon='info-sign')).add_to(folium_map)

    tourist_data = pd.read_csv("Visit Rate Ranking.csv")
    tourist_data = tourist_data.dropna()
    tourist_data.head()

    for index, row in tourist_data.iterrows():
        folium.CircleMarker(
            location=[float(row['Longitude']), float(row['Latitude'])],
            popup=row['Prefecture'],
            radius=3*row['2015'],
            color='#3186cc',
            fill=True,
            fill_color='#3186cc').add_to(folium_map)
    folium_map.save("templates/my_map.html")
    return render_template("my_map.html")

@app.route("/map2014", methods = ["GET"])
def resultmap2014():
    film_data = pd.read_csv("film.csv")
    film_data = film_data.dropna()
    film_data.head()

    for index, row in film_data.iterrows():
        folium.Marker(
            location=[float(row['Longitude']),float(row['Latitude'])],
            popup = row['Film'],
            icon=folium.Icon(color='red', icon='info-sign')).add_to(folium_map)

    tourist_data = pd.read_csv("Visit Rate Ranking.csv")
    tourist_data = tourist_data.dropna()
    tourist_data.head()

    for index, row in tourist_data.iterrows():
        folium.CircleMarker(
            location=[float(row['Longitude']), float(row['Latitude'])],
            popup=row['Prefecture'],
            radius=3*row['2014'],
            color='#3186cc',
            fill=True,
            fill_color='#3186cc').add_to(folium_map)
    folium_map.save("templates/my_map.html")
    return render_template("my_map.html")

@app.route("/map2013", methods = ["GET"])
def resultmap2013():
    film_data = pd.read_csv("film.csv")
    film_data = film_data.dropna()
    film_data.head()

    for index, row in film_data.iterrows():
        folium.Marker(
            location=[float(row['Longitude']),float(row['Latitude'])],
            popup = row['Film'],
            icon=folium.Icon(color='red', icon='info-sign')).add_to(folium_map)

    tourist_data = pd.read_csv("Visit Rate Ranking.csv")
    tourist_data = tourist_data.dropna()
    tourist_data.head()

    for index, row in tourist_data.iterrows():
        folium.CircleMarker(
            location=[float(row['Longitude']), float(row['Latitude'])],
            popup=row['Prefecture'],
            radius=3*row['2013'],
            color='#3186cc',
            fill=True,
            fill_color='#3186cc').add_to(folium_map)
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
