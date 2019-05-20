import numpy as np

# https://www.numpy.org/
# List
numbers = [10, 20, 30, 40, 50]
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # List of List | 2-D

print(numbers, len(numbers)) # 5
print(data, len(data))       # 3

# Numpy Array

# Passing List as Input to numpy array function
a1 = np.array([10, 20, 30, 40, 50])
print(a1)
print(type(a1))
print(a1.shape)

print()

# Passing Tuple as Input to numpy array function
a2 = np.array((10, 20, 30, 40, 50))
print(a2)
print(type(a2))
print(a2.shape)

print()

# Passing Set as Input to numpy array function
a3 = np.array({10, 20, 30, 40, 50, 30, 20})
print(a3)
print(type(a3))
print(a3.shape)

print()

employees = {101:"John", 201:"Jennie", 301:"Jack"}
a4 = np.array(employees)
print(a4)
print(type(a4))
print(a4.shape)