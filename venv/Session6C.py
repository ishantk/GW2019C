# Nested Loops
# Loops within Loops

"""
for i in range(1,4):
    print("i is:",i)

    for j in range(1,4):
        # print("j is:",j)
        # print(j)
        print(j, end=" ")

    print()
"""
for i in range(1, 6):

    for j in range(1, i+1):
        print(j, end=" ")

    print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

Print below Pattern:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

And Find Sum of the above numbers ?



"""