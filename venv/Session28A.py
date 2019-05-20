import numpy as np

a = [10, 20, 30, 40, 50]
print(type(a))
a1 = np.array(a)
print(a1)
print(type(a1))
print(a1.shape) # (5,)

b = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
a2 = np.array(b)
print(a2)
print(a2.shape) # (3, 3)
print(type(a2))

c = [
     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
     [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ]
a3 = np.array(c)
print(a3)
print(a3.shape)
print(type(a3))