from random import *
from time import *
#Program that compares the time usage
#of bolo-sort and insertion-sort
seed()
oldX = []
count= 0
bogoCount = 0

def randomize():
    for i in range(0, 1000):
        oldX.append(randint(0, 100))

def inorder(x):
    i = 0
    j = len(x)
    while i + 1 < j:
        if x[i] > x[i + 1]:
            return False
        i += 1
    return True

def bogo(x):
    global bogoCount
    while not inorder(x):
        bogoCount+=1
        shuffle(x)
    return x


def insertionsort(x):
    global count
    for j in range(1,len(x)):
        key = x[j]
        i = j-1
        count+=1
        while (i > -1) and key < x[i]:
            count+=1
            x[i+1]=x[i]
            i=i-1
        x[i+1] = key
    return x





randomize()
startInsertion = time()
print("\nInsertion Sort:")
print("Before: ", oldX)
y = insertionsort(oldX)
print("After: ", y)
print("%.2f seconds" % (time() - startInsertion))
print("Count:", count)

oldX = []
randomize()
startBogo = time()
print("\nBogo Sort:")
print("Before: ", oldX)
x = bogo(oldX)
print("After: ", x)
print("%.2f seconds" % (time() - startBogo))
print("Count", bogoCount)
