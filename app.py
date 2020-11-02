from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

# Sorting and searching algorithms from other program
from helpers import *

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

@app.route("/", methods=["GET"])
def index():
    '''Home Page where user can choose which sort they want'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("index.html")

@app.route("/sorts", methods=["GET"])
def sorts():
    '''Display page for sorts'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("sorts.html")

@app.route("/searches", methods=["GET"])
def searches():
    '''Display page for searches'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("searches.html")

@app.route("/bubbleSort", methods=["GET", "POST"])
def bubbleSort():
    '''Bubble sort page'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("bubbleSort.html")

@app.route("/mergeSort", methods=["GET", "POST"])
def mergeSort():
    '''Merge sort page'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("mergeSort.html")

@app.route("/linearSearch", methods=["GET", "POST"])
def linearSearch():
    '''Linear Search page'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("linearSearch.html")

@app.route("/binarySearch", methods=["GET", "POST"])
def binarySearch():
    '''Binary Search page'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("binarySearch.html")
    # List of numbers that user inputted
    lst = request.form.get("bSearchInput").split(",")
    # Process list of values
    while "" in lst:
        lst.remove("")
    #lst = x) for x in lst]
    # Value to search for
    val = request.form.get("bSearchVal")
    # Perform binary search on user data and store information about whether the value was found, how many steps it took and the first occuring index of the value
    steps = bSearch(lst, val)

    return render_template("binarySearch.html", searchDone=True, res=val, steps=steps)
