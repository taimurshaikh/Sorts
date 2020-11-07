import random
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

def bSort(vals):
    if not isNumList(vals):
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

# Temporary steps implementation with global variable
mSortSteps = 0
def mSort(vals):
    def merge(l1, l2):
        res = []
        while l1 and l2:
            if l1[0] > l2[0]:
                res.append(l2.pop(0))
            else:
                res.append(l1.pop(0))
        while l1:

            res.append(l1.pop(0))
        while l2:

            res.append(l2.pop(0))
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
    vals = convertToInts(vals)
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
