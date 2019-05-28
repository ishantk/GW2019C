import numpy as np
import pandas as pd

# Python List
numbers = [10, 20, 30, 40, 50]
print(numbers, type(numbers))

print()

# Numpy Array
nArr = np.array([10, 20, 30, 40, 50])
print(nArr, type(nArr))

print()

series1 = pd.Series([10, 20, 30, 40, 50])
series1 = pd.Series((10, 20, 30, 40, 50))
print(series1, type(series1))

print()

# Create Series from List
series2 = pd.Series(numbers)
print(series2, type(series2))

print()

# Create Series from Numpy Array
series3 = pd.Series(nArr)
print(series3, type(series3))

