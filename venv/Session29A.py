import numpy as np

arr = np.arange(10, 51, 3)
print("arr is:",arr)
print("arr shape is:",arr.shape)
print("arr shape[0] is:",arr.shape[0])
print("arr length is:",len(arr))

# Access Elements
print(arr[3:]) # 3rd index to last index
print(arr[:5]) # 0th index to 4th index
print(arr[3:5]) # 3rd index to 4th index
# Explore negative index

# slice develops a pattern which can be passed to array to fetch corresponding indexes
slices = slice(1, 10, 2) # -> 1, 3, 5, 7, 9
print(slices)
print(type(slices))
print(arr[slices])

data = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
arr2D = np.array(data)
print(arr2D)
print(arr2D[1])         # 4, 5, 6
print(arr2D[1][1])      # 5
print(arr2D.shape)      # (3, 3)
print(arr2D.shape[0])   # 3
print(arr2D.shape[1])   # 3

print(arr2D[0:2])       # [1, 2, 3] [4, 5, 6]
print(arr2D[0:2, 0:2])  # [1, 2] [4, 5]

# Write the same for arr3D !!