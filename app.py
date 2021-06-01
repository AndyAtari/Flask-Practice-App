from flask import Flask
from datetime import date, datetime, time 
from flask import render_template
from flask_babel import Babel 
from flask_babel import format_datetime
import re


app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def home():
    return "My Flask App! Cool Beans!"

@app.route("/hello/<name>")
@app.route("/hello/")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        babel_date = format_datetime(datetime.now())
    )
