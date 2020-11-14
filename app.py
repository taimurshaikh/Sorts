from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

# Sorting and searching algorithms from other program
from helpers import *
from datetime import datetime
import time
import random
import csv
import os

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

    # If user wants to input a file
    chooseFile = request.form.get("csvFile")
    if chooseFile:
        lst = validateFile(chooseFile)
        if not lst:
            return render_template("bubbleSort.html", done=True, steps=lst)

    else:
        # List of numbers that user inputted
        lst = request.form.get("bSortInput").split(",")

        isRandom = request.form.get("random")
        # If random array, then the user must enter 3 values: length,startrange,endrange
        if isRandom == "random":
            while "" in lst:
                lst.remove("")
            while " " in lst:
                lst.remove(" ")
            if len(lst) != 3 or not isNumList(lst) or not lst:
                return render_template("bubbleSort.html", done=True, steps=-1)
            lst = convertToInts(lst)
            length, start, end = lst[0], lst[1], lst[2]
            if end < start:
                return render_template("bubbleSort.html", done=True, steps=-1)
            randomLst = [random.randrange(start,end) for x in range(length)]
            lst = randomLst
    while "" in lst:
        lst.remove("")
    while " " in lst:
        lst.remove(" ")
    # Use this to track how much time the algorithm takes
    startTime = time.time_ns()
    # Perform bubble sort on user data and store information about how many steps it took and the first occuring index of the value
    (res, steps) = bSort(lst)
    order = request.form.get("order")
    if order == "descending" and not isinstance(res, int):
        res = res[::-1]
    endTime = time.time_ns()
    timeTaken = endTime - startTime
    if not timeTaken:
        # Making timeTaken equal the string we want to display if the algorithm was really fast
        timeTaken = "less than 1"

    return render_template("bubbleSort.html", done=True, res=res, steps=steps, timeTaken=timeTaken)

@app.route("/sorts/mergeSort", methods=["GET", "POST"])
def mergeSort():
    '''Merge sort page'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("mergeSort.html")

    # POST REQUEST
    # If user wants to input a file
    chooseFile = request.form.get("csvFile")
    if chooseFile:
        lst = validateFile(chooseFile)
        if not lst:
            return render_template("bubbleSort.html", done=True, steps=lst)
    else:
        # First we must check if the user wants to generate a random array
        isRandom = request.form.get("random")
        # List of numbers that user inputted
        lst = request.form.get("mSortInput").split(",")
        try:
            lst = convertToInts(lst)
        except:
            res = -1

        # If random array, then the user must enter 3 values: length,startrange,endrange
        if isRandom == "random":
            while " " in lst:
                lst.remove(" ")
            while "" in lst:
                lst.remove("")
            if len(lst) != 3 or not isNumList(lst) or not lst:
                return render_template("mergeSort.html", done=True, res=-1)
            lst = convertToInts(lst)
            length, start, end = lst[0], lst[1], lst[2]
            if end < start:
                return render_template("mergeSort.html", done=True, steps=-1)
            randomLst = [random.randrange(start,end) for x in range(length)]
            lst = randomLst

    # Process list of values
    while " " in lst:
        lst.remove(" ")
    while "" in lst:
        lst.remove("")
    # Use this to track how much time the algorithm takes
    startTime = time.time_ns()
    # Perform mergesort sort on user data
    res = mSort(lst)
    steps = mSortSteps
    endTime = time.time_ns()
    timeTaken = endTime - startTime
    if not timeTaken:
        # Making timeTaken equal the string we want to display if the algorithm was really fast
        timeTaken = "less than 1"
    order = request.form.get("order")
    if order == "descending" and not isinstance(res, int):
        res = res[::-1]
    return render_template("mergeSort.html", done=True, res=res, steps=steps, timeTaken=timeTaken)

@app.route("/searches/linearSearch", methods=["GET", "POST"])
def linearSearch():
    '''Linear Search page'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("linearSearch.html")

    # POST REQUEST
    # If user wants to input a file
    chooseFile = request.form.get("csvFile")
    if chooseFile:
        lst = validateFile(chooseFile)
        if not lst:
            return render_template("linearSearch.html", done=True, steps=lst)
    else:
        # List of numbers that user inputted
        lst = request.form.get("lSearchInput").split(",")
        # Check if the user wants to generate a random array
        isRandom = request.form.get("random")
        # If random array, then the user must enter 3 values: length,startrange,endrange
        if isRandom == "random":
            while " " in lst:
                lst.remove(" ")
            while "" in lst:
                lst.remove("")
            if len(lst) != 3 or not isNumList(lst) or not lst:
                return render_template("linearSearch.html", done=True, steps=-1)
            lst = convertToInts(lst)
            length, start, end = lst[0], lst[1], lst[2]
            if end < start:
                return render_template("linearSearch.html", done=True, steps=-1)
            randomLst = [random.randrange(start,end) for x in range(length)]
            lst = randomLst

    # Value to search for
    val = request.form.get("lSearchVal")
    # Process list of values
    while " " in lst:
        lst.remove(" ")
    while "" in lst:
        lst.remove("")
    startTime = time.time_ns()
    # Perform linear search on user data and store information about whether the value was found, how many steps it took and the first occuring index of the value
    steps = lSearch(lst, val)
    print(steps)
    endTime = time.time_ns()
    timeTaken = endTime - startTime
    if not timeTaken:
        timeTaken = "less than 1"
    ind = None
    try:
        ind = lst.index(int(val))
    except:
        pass
    return render_template("linearSearch.html", done=True, val=val, steps=steps, ind=ind, timeTaken=timeTaken)

@app.route("/searches/binarySearch", methods=["GET", "POST"])
def binarySearch():
    '''Binary Search page'''
    # GET REQUEST
    if request.method == 'GET':
        return render_template("binarySearch.html")

    # POST REQUEST
    # If user wants to input a file
    chooseFile = request.form.get("csvFile")
    if chooseFile:
        lst = validateFile(chooseFile)
        if not lst:
            lst -= 1
            return render_template("binarySearch.html", done=True, steps=lst)
        lst = mSort(lst)
    else:
        # List of numbers that user inputted
        lst = request.form.get("bSearchInput").split(",")
        # Check if the user wants to generate a random array
        isRandom = request.form.get("random")
        # If random array, then the user must enter 3 values: length,startrange,endrange
        if isRandom == "random":
            while " " in lst:
                lst.remove(" ")
            while "" in lst:
                lst.remove("")
            if len(lst) != 3 or not isNumList(lst) or not lst:
                return render_template("binarySearch.html", done=True, steps=-2)
            lst = convertToInts(lst)
            length, start, end = lst[0], lst[1], lst[2]
            if end < start:
                return render_template("binarySearch.html", done=True, steps=-2)
            randomLst = mSort([random.randrange(start,end) for x in range(length)])
            lst = randomLst

    lst = convertToInts(lst)
    # Value to search for
    val = request.form.get("bSearchVal")
    # Process list of values
    while " " in lst:
        lst.remove(" ")
    while "" in lst:
        lst.remove("")
    startTime = time.time_ns()
    # Perform binary search on user data and store information about whether the value was found, how many steps it took and the first occuring index of the value
    steps = bSearch(lst, val)
    endTime = time.time_ns()
    timeTaken = endTime - startTime
    if not timeTaken:
        timeTaken = "less than 1"
    ind = None
    try:
        ind = lst.index(int(val))
    except:
        ind = "not found"
    return render_template("binarySearch.html", done=True, val=val, steps=steps, ind=ind, timeTaken=timeTaken)
