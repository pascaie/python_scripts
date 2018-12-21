# examples and tests using the numpy package
# 1) create a simple numpy array
# 2) create a rank 2 numpy array
# 3) functions: ndim (rank), shape, size, type

import numpy as np

# create and display a numpy array
npArray = np.array([1, 2, 3, 4])
print(npArray)

# create a numpy array of rank 2
npArray2 = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8]])
print(npArray2)
print(npArray2[1, 2])  # elenment in the 2nd block at position 3: 7

# RANK of the array: ndim
print('First array has rank equal to: ' + str(npArray.ndim))
print('First array has rank equal to: ' + str(npArray2.ndim))

# SHAPE: number of rows and columns
print(npArray2.shape)  # returns something like (n, m)
print('Number of columns: ' + str(npArray2.shape[1]))

# SIZE: number of elements in the array
print('Total number of elements: ' + str(npArray2.size))

# TYPE of the npArray
print(type(npArray2))
