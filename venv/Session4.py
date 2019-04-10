# Operators
# They shall perform Operation on Data

# Arithmetic Operators
# +, -, *, /, //, %
n1 = 10
n2 = 3

n3 = n1 + n2
n4 = n1 - n2
n5 = n1 * n2
n6 = n1 / n2
n7 = n1 // n2
n8 = n1 % n2

print("n3 is:",n3)
print("n4 is:",n4)
print("n5 is:",n5)
print("n6 is:",n6)
print("n7 is:",n7)
print("n8 is:",n8)

# Assignment Operators
# = | Move RHS into LHS (Write and Update)
a = 11
a += 10 # a = a + 10
a *= 3  # a = a * 3
a %= 5  # a = a % 5 -> 3
a += 1
a -= 1

print("a is:",a)

# Conditional Operators | True or False
# >, <, >=, <=, ==, !=
x = 10
y = 20
z = 30
print("is x greater than y?",x>y)
print(x>y)
print(x==y)
print(x!=y)

# Logical Operators
# and or

print(z>y and z>x)
print(y>x and y>z)
print(y>x or y>z)
"""
    And Operation
    T T   T
    T F   F
    F T   F
    F F   F
    
    OR Operation
    T T   T
    T F   T
    F T   T
    F F   F
"""

p = 3
q = p ** 3 # p power 3
print(q)

# Bitwise Operators
# binary means 2
# 128 64 32 16 8 4 2 1       -> 8Bits (1Byte)
#              1 0 1 1
#      1  0  0 0 0 1 1
n1 = 8
n2 = 11
print(n1)       # 8
print(n2)       # 11
print(bin(n1))  # 1 0 0 0
print(bin(n2))  # 1 0 1 1

# AND Operation
n3 = n1 & n2    # 1 0 0 0
# OR Operation
n4 = n1 | n2    # 1 0 1 1
#XOR Operation
n5 = n1 ^ n2    # 0 0 1 1
print(n3)
print(n4)
print(n5)

# Shift Operators
a = 11          # 1 0 1 1
b = 3           # _ _ _ 1 -> 0 0 0 1
c = a >> b      # 1
d = a << b      # 0 0 0 0 1 0 1 1 -> 0 1 0 1 1 0 0 0
print("c is:",c)
print("d is:",d)

print(d is 88)      # ==
print(d is not 88)  # !=

# Assignment:
# Take integer number input from User.
# And tell if its a prime number or not ?
# 3 -> True/False