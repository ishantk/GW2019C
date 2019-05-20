import numpy as np

a1 = np.ones(8)
a1[2] = 333
print(a1[0])
print(a1)
print(a1.shape)
print(len(a1))

# for i in range(len(a1)):
#     print(a1[i])

for elm in a1:
    print(elm)

print()

a2 = np.zeros(8)
print(a2)
print(a2.shape)

print()

a3 = a1.reshape(2, 2, 2) # ReShape array for a new array
print(a1)

print()

print(a3)

print()

a4 = a3.ravel() # Faltten Array to 1-D Array
print(a4)

"""
   n-queen Problem : No Googling :p
   0   1   0   0
   0   0   1   0
   1   0   0   0
   0   0   0   1
   
   Place 4 Queens on the chessboard
   1. No queen in same row
   2. No queen in same column
   3. No queen in same diagonal left or right 

"""