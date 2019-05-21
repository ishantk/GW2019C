import numpy as np

# Read txt file using numpy
arr = np.loadtxt("data.txt")
print(arr)
print(arr.shape)

arr = np.arange(10, 200, 10)
print(arr)
print(arr.shape)
print(len(arr))

np.savetxt("data1.txt", arr)

# Read txt file containing data in array format i.e. 2 d array
# 1. Rotate array to left
#    90, 180
# 2. Save it in another file