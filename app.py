from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

# Sorting and searching algorithms from other program
from helpers import *
from datetime import datetime
import time
import random
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

@app.route("/sorts/bubbleSort", methods=["GET", "POST"])
def bubbleSort():
    '''Bubble sort page'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("bubbleSort.html")

    # POST REQUEST
    # First we must check if the user wants to generate a random array
    random = request.form.get("random")
    # List of numbers that user inputted
    lst = request.form.get("bSortInput").split(",")
    # Process list of values
    # Use this to track how much time the algorithm takes
    startTime = time.time_ns()
    # Perform bubble sort on user data and store information about how many steps it took and the first occuring index of the value
    (res, steps) = bSort(lst)
    endTime = time.time_ns()
    timeTaken = endTime - startTime
    if not timeTaken:
        # Making timeTaken equal the string we want to display if the algorithm was really fast
        timeTaken = "less than 1"
    order = request.form.get("order")
    if order == "descending":
        res = res[::-1]
    return render_template("bubbleSort.html", sortDone=True, res=res, steps=steps, timeTaken=timeTaken)

@app.route("/sorts/mergeSort", methods=["GET", "POST"])
def mergeSort():
    '''Merge sort page'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("mergeSort.html")

    # POST REQUEST
    # List of numbers that user inputted
    lst = request.form.get("mSortInput").split(",")
    # Process list of values
    while " " in lst:
        lst.remove(" ")
    while "" in lst:
        lst.remove("")
    try:
        lst = convertToInts(lst)
    except:
        res = -1
    # Use this to track how much time the algorithm takes
    startTime = time.time_ns()
    # Perform mergesort sort on user data
    res = mSort(lst)
    endTime = time.time_ns()
    timeTaken = endTime - startTime
    if not timeTaken:
        # Making timeTaken equal the string we want to display if the algorithm was really fast
        timeTaken = "less than 1"
    order = request.form.get("order")
    if order == "descending":
        res = res[::-1]
    return render_template("mergeSort.html", sortDone=True, res=res, timeTaken=timeTaken)

@app.route("/searches/linearSearch", methods=["GET", "POST"])
def linearSearch():
    '''Linear Search page'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("linearSearch.html")

    # POST REQUEST
    # List of numbers that user inputted
    lst = request.form.get("lSearchInput").split(",")
    # Process list of values
    while " " in lst:
        lst.remove(" ")
    while "" in lst:
        lst.remove("")
    # Value to search for
    val = request.form.get("lSearchVal")
    startTime = time.time_ns()
    # Perform linear search on user data and store information about whether the value was found, how many steps it took and the first occuring index of the value
    steps = lSearch(lst, val)
    endTime = time.time_ns()
    timeTaken = endTime - startTime
    if not timeTaken:
        timeTaken = "less than 1"
    ind = None
    if steps != False and steps > 0:
        ind = lst.index(val)
    return render_template("linearSearch.html", searchDone=True, val=val, steps=steps, ind=ind, timeTaken=timeTaken)

@app.route("/searches/binarySearch", methods=["GET", "POST"])
def binarySearch():
    '''Binary Search page'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("binarySearch.html")

    # POST REQUEST
    # List of numbers that user inputted
    lst = request.form.get("bSearchInput").split(",")
    # Process list of values
    while " " in lst:
        lst.remove(" ")
    while "" in lst:
        lst.remove("")
    # Value to search for
    val = request.form.get("bSearchVal")
    startTime = time.time_ns()
    # Perform binary search on user data and store information about whether the value was found, how many steps it took and the first occuring index of the value
    steps = bSearch(lst, val)
    endTime = time.time_ns()
    timeTaken = endTime - startTime
    if not timeTaken:
        timeTaken = "less than 1"
    ind = None
    if steps != False and steps >= 0:
        lst = convertToInts(lst)
        ind = lst.index(int(val))
    return render_template("binarySearch.html", searchDone=True, val=val, steps=steps, ind=ind, timeTaken=timeTaken)
