import os
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('home.html', title="Home Page", header="Hello World!!!")

@app.route("/about")
def about():
  return render_template('about.html', title="About Me", header="About Me")