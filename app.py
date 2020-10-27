from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

from helpers import Sorts

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Initialize sorter class that holds all sorting algorithms
sorter = Sorts()

@app.route("/", methods=["GET", "POST"])
def index():
    '''Home Page where user can choose which sort they want'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("index.html")
    # POST REQUEST
    pass

@app.route("/bSort", methods=["GET", "POST"])
def bSort():
    pass

@app.route("/mSort", methods=["GET", "POST"])
def mSort():
    pass

@app.route("/lSearch", methods=["GET", "POST"])
def lSearch():
    pass

@app.route("/bSearch", methods=["GET", "POST"])
def bSearch():
    pass
