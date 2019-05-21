import numpy as np
a1 = np.arange(10, 31)
print(a1)

a2 = np.arange(10, 31, 3)
print(a2)

# create a 2-dim array of 3X3
a3 = np.zeros((3,3)) # a4 = np.ones((3,3))
print(a3)

a3[0][1] = 100
print(a3)

print()

a4 = np.linspace(0, 21, 4)
print(a4)

numbers = [11, 22, 33, 44, 55]
a5 = np.asarray(numbers)
print(a5)

# Explore : array vs asarray