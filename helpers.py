import random, os, csv
def isSorted(lst):
    # Check if list is sorted or not
    for i in range(len(lst)):
        if not i:
            continue
        if lst[i] < lst[i-1]:
            print(f"{lst[i]} less than {lst[1+1]}")
            return False
    return True

def isNumList(lst):
    for i in lst:
        try:
            i = int(i)
        except:
            return False
    return True

def convertToInts(lst):
    return [int(x) for x in lst]

def validateFile(filename):
    if filename[-3:] != "csv":
        return -2
    with open(os.path.abspath(filename)) as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i > 0 or not isNumList(row):
                return -2
            return convertToInts(row)

def bSort(vals):
    if not isNumList(vals) or not vals:
        return -1, -1
    vals = convertToInts(vals)
    steps = 0
    length = len(vals)
    for i in range(length):
        for j in range(length):
            if j == 0:
                continue
            if vals[j-1] > vals[j]:
                steps += 1
                vals[j-1], vals[j] = vals[j], vals[j-1]
    return (vals, steps)

# Temporary steps implementation with global variable (Really bad lol)
mSortSteps = 0
def mSort(vals):
    global mSortSteps
    if not vals:
        return -1
    def merge(l1, l2):
        global mSortSteps
        res = []
        while l1 and l2:
            mSortSteps += 1
            if l1[0] > l2[0]:
                res.append(l2.pop(0))
            else:
                res.append(l1.pop(0))
        while l1:
            res.append(l1.pop(0))
        while l2:
            res.append(l2.pop(0))
        mSortSteps += 1
        return res
    if not isNumList(vals):
        return -1
    if len(vals) == 1:
        return vals
    midpoint = len(vals) // 2
    firstHalf = mSort(vals[:midpoint])
    secondHalf = mSort(vals[midpoint:])
    return merge(firstHalf, secondHalf)

def lSearch(vals, val):
    if not isNumList(vals) or not isNumList([val]):
        return -1
    vals = convertToInts(vals)
    val = int(val)
    steps = 0
    for i in vals:
        steps += 1
        if i == val:
            return steps
    return False

def bSearch(vals, val, steps=0):
    if not isNumList(vals) or not isNumList([val]):
        return -2
    if not isSorted(vals):
        return -1
    val = int(val)
    if len(vals) == 1:
        if vals[0] == val:
            steps += 1
            return steps
        return False
    midpoint = len(vals) // 2
    if vals[midpoint] == val:
        steps += 1
        return steps
    if val < vals[midpoint]:
        steps += 1
        return bSearch(vals[:midpoint], val, steps)
    elif val > vals[midpoint]:
        steps += 1
        return bSearch(vals[midpoint:], val, steps)

print(bSearch([1,3,5,67,56543], 5))
