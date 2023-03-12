import csv
import sys
import time
import numpy as np

sys.set_int_max_str_digits(100000000)
np.set_printoptions(threshold=sys.maxsize)

filename = 'List_Array.csv'
file = open(filename, 'w', newline="")
csvwriter = csv.writer(file)
csvwriter.writerow(["Factorial", "DataType", "Before", "After", "Size"])


def get_time():
    return time.time()


def factorial_list(num):
    list_fact = []
    fact = 1
    for k in range(1, num + 1):
        fact = fact * k
        list_fact.append(fact)
    return list_fact


def factorial_numpy(num):
    np_fact = np.zeros(num + 1)
    fact = 1.0
    for f in range(1, num + 1):
        fact = fact * f
        np_fact[f] = fact
    return np_fact


for i in range(10000, 10010):
    x = get_time()
    numpy_array = factorial_numpy(i)
    y = get_time()
    csvwriter.writerow([i, "Array", x, y, numpy_array.itemsize * numpy_array.size])
    q = get_time()
    list_fact = factorial_list(i)
    p = get_time()
    csvwriter.writerow([i, "List", q, p, sys.getsizeof(list) * len(list_fact)])
