import os

import folium
from folium import plugins

#we added the folium extension - they had to be downloaded as a package - such that we could use the interactive map function

import pandas as pd

#panda is also part of the interactive map

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

#the folium map is centered in a certain location; we choose the location information for Japan and start with a zoomed out versionn
folium_map = folium.Map(location= [34.6937, 135.5023], zoom_start= 7)

#our mainpage displays the basic information of our project
@app.route("/", methods = ["GET"])
def choose_std():
    return render_template("standard.html")

#datatable provides us with what information we used
@app.route("/dtable", methods = ["GET"])
def choose_dtable():
    return render_template("dtable.html")

# this page allows to choose the tourist information per year
@app.route("/year", methods = ["GET"])
def template():
    return render_template("tourism.html")

#The following is coding for interactive map with data overlay
@app.route("/map2017", methods = ["GET"])
def resultmap2017():
    # we first, import the csv of the data that we need; they were collected and cleaned in advance
    film_data = pd.read_csv("film.csv")
    film_data = film_data.dropna()
    film_data.head()

    #we use a for loop to generate red icons that demonstrate where movies were shot
    for index, row in film_data.iterrows():
        folium.Marker(
            location=[float(row['Longitude']),float(row['Latitude'])],
            popup = row['Film'],
            icon=folium.Icon(color='red', icon='info-sign')).add_to(folium_map)

    #same cleaned, organized data which will be used
    tourist_data = pd.read_csv("Visit Rate Ranking.csv")
    tourist_data = tourist_data.dropna()
    tourist_data.head()

    #we use a for loop to generate circle overlays that will demonstrate the proportion of tourists per district
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
