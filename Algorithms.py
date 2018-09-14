from random import *
from time import *
import numpy as np
import matplotlib.pyplot as plt

seed()
x = []
count = 0


def randomize(size):
    for i in range(0, size):
        x.append(randint(0, 100))


def inorder(x):
    i = 0
    j = len(x)
    while i + 1 < j:
        if x[i] > x[i + 1]:
            return False
        i += 1
    return True


def bogo(x):
    while not inorder(x):
        countN()
        shuffle(x)
    return x


def insertionsort(x):
    for j in range(1, len(x)):
        key = x[j]
        i = j - 1
        countN()
        while (i > -1) and key < x[i]:
            countN()
            x[i + 1] = x[i]
            i = i - 1
        x[i + 1] = key
    return x

def countN():
    global count
    count = count +1

def runBogo(size):
    global x
    global count
    x.clear()
    randomize(size)
    count = 0
    print("\nBogo Sort (", size, "):")
    print("Before: ", x)
    startBogo = time()
    x = bogo(x)
    duration = time() - startBogo
    print("After: ", x)
    print("%.2f seconds" % (duration))
    print("Count", count)
    return duration

def runInsertion(size):
    global x
    global count
    x.clear()
    randomize(size)
    count = 0
    print("\nInsertion Sort (", size, "):")
    print("Before: ", x)
    startInsertion = time()
    x = insertionsort(x)
    duration = time() - startInsertion
    print("After: ", x)
    print("%.2f seconds" % (duration))
    print("Count:", count)
    return duration

insertionDurations = []
insertionSize = []
bogoDurations = []
bogoSize = []

for size in range(1, 1000):
    insertionDurations.append(runInsertion(size))
    insertionSize.append(size)

print("Insertion times:", insertionDurations)
plt.plot(insertionSize, insertionDurations)
plt.title("Insertion-sort")
plt.xlabel("Number of elements")
plt.ylabel("Time in seconds")

for size in range(1, 11):
    bogoDurations.append(runBogo(size))
    bogoSize.append(size)

print("Bogo times", bogoDurations)

plt.figure(2)
plt.plot(bogoSize, bogoDurations)
plt.title("Bogo-sort")
plt.xlabel("Number of elements")
plt.ylabel("Time in seconds")
plt.show()
