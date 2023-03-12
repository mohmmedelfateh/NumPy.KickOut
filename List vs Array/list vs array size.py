import numpy as np
import time
import sys

# Let's try to create a numpy Array of 1000 elements:-
numpy_array = np.arange(1000)
# print(numpy_array.itemsize) # Gives the Size of one element
# print(numpy_array.size) # Gives the length of the Array
print("Size in Bytes for Numpy Array of 1000 elements:", numpy_array.itemsize * numpy_array.size)

# Let's try to create a list of 1000 elements :-
list = range(1000)

# print(sys.getsizeof(list)) # Gives the size of One element of the List
# print(len(list))# Gives the length of the List
print("Size in Bytes for List of 1000 Elements:", sys.getsizeof(list) * len(list))
