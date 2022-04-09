from flask import Flask, render_template, request
from datetime import datetime
import re

app = Flask(__name__)


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
