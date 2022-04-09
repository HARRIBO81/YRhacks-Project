import json
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import key 

app = Flask(__name__)
key = key.getEnv()


## EMPTY HTML FILES
@app.route("/")
def home():
    return render_template("index.html", prediction = None)

@app.route("/about")
def about():
    return render_template("about.html")
    

##passes an image into our ML Model and 
@app.route("/submit", methods = ['POST'])
def submit(name = None):
    if request.method == 'POST':
        img = request.files['image name']  ## IMAGE NAME DEPENDS ON NAME INSIDE THE HTML INPUT ELEMENT!!
        path = "static/predicting" +img.name
        img.save(path)
    
    ##put call to ML model right here (replace null)
    prediction = None
    
    return render_template("index.html", prediction = prediction)

##GOOGLE MAPS TESTING

@app.route("/maps/")
def mapInit():
    return render_template("maps.html")


@app.route("/maps/<string:query>", methods = ['POST'])
def maps(query):
    payload = {"key":key, "query":query}
    req = request.post(search_url, params=payload)
    searchJson = req.json()
    
    placeId = searchJson["results"][0]["place_id"]
    
    url = ""
    return jsonify({'result': url})

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"
