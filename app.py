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

@app.route("/sorts/bubbleSort", methods=["GET", "POST"])
def bubbleSort():
    '''Bubble sort page'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("bubbleSort.html")

    # POST REQUEST
    # List of numbers that user inputted
    lst = request.form.get("bSortInput").split(",")
    # Process list of values
    #while " " in lst:
    #    lst.remove(" ")
    while "" in lst:
        lst.remove("")
    lst = convertToInts(lst)
    # Perform bubble sort on user data and store information about whether the value was found, how many steps it took and the first occuring index of the value
    (res, steps) = bSort(lst)

    return render_template("bubbleSort.html", sortDone=True, res=res, steps=steps)

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
    lst = convertToInts(lst)
    # Perform merge sort on user data and store information about whether the value was found, how many steps it took and the first occuring index of the value
    res = mSort(lst)

    return render_template("mergeSort.html", sortDone=True, res=res)

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
    # Perform linear search on user data and store information about whether the value was found, how many steps it took and the first occuring index of the value
    steps = lSearch(lst, val)
    if steps:
        ind = lst.index(val)
    return render_template("linearSearch.html", searchDone=True, val=val, steps=steps, ind=ind)

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
    lst = convertToInts(lst)
    # Value to search for
    val = request.form.get("bSearchVal")
    # Perform binary search on user data and store information about whether the value was found, how many steps it took and the first occuring index of the value
    steps = bSearch(lst, val)
    if steps:
        print(lst)
        ind = lst.index(int(val))
    return render_template("binarySearch.html", searchDone=True, val=val, steps=steps, ind=ind)
