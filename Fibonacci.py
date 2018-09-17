from random import *
from time import *
import matplotlib.pyplot as plt


# n: nonnegativ integer
# output is the nth Fibonacci number
def iterative_fibonacci(n):
    if n == 0:
        return 0
    else:
        x = 0
        y = 1
        for i in range(1, n):
            z = x + y
            x = y
            y = z
        return y


# n: nonnegative integer
# output: fibonacci(n)/the nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def mergesort(list):
    n = len(list)
    list1 = []
    list2 = []
    if n > 1:
        m = n // 2
        for i in range(0, m):
            list1.append(list[i])
        for i in range(m, n):
            list2.append(list[i])

        list = merge(mergesort(list1), mergesort(list2))
    return list


def merge(list1, list2):
    merged_list = []
    while (len(list1) > 0) & (len(list2) > 0):
        if list1[0] < list2[0]:
            merged_list.append(list1[0])
            del (list1[0])
            if len(list1) == 0:
                del list1
                merged_list.extend(list2)
                del list2
                break
        else:
            merged_list.append(list2[0])
            del (list2[0])
            if len(list2) == 0:
                del list2
                merged_list.extend(list1)
                del list1
                break
    return merged_list


def randomize(size):
    for i in range(0, size):
        a.append(randint(0, 10000))


def run_merge_sort(size):
    global a
    a.clear()
    randomize(size)
    # print("\n(", size, ")", "Before: ", a)
    # sleep(0.01)
    start_time = time()
    a = mergesort(a)
    duration = time() - start_time
    # sleep(0.01)
    # print("After: ", a)
    # print("%.2f seconds" % (duration))
    return duration


print("Recursive Fibonacci:\nf(8)=", fibonacci(8))
print("\nIterative Fibonacci:\nf(8)=", iterative_fibonacci(8))

a = []
duration = []
elements = []
for size in range(1, 1000):
    duration.append(run_merge_sort(size))
    elements.append(size)

plt.plot(elements, duration)
plt.title("Merge-sort")
plt.xlabel("Number of elements")
plt.ylabel("Time in seconds")
plt.show()
