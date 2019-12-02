import os

import folium
from folium import plugins

import requests

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

def spefcity():
    #attempted to add location marker
    folium.Marker(
    location=[35.6762, 139.6503],
    popup='Osaka',
    icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(folium_map)

    folium_map.save("templates/my_map.html")
    return render_template("my_map.html")

def trackpop():
    #can be used for popularity tracking
    folium.CircleMarker(
    location=[35.6762, 139.6503],
    radius=50,
    popup='Osaka 20##',
    color='#3186cc',
    fill=True,
    fill_color='#3186cc'
    ).add_to(folium_map)

    folium_map.save("templates/my_map.html")
    return render_template("my_map.html")