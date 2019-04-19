a = 10
b = a
a = b * 2

print("a is:",a) # 20
print("b is:",b) # 10

x = [10, 20, 30, 40, 50]
y = x

print("x is:",x,"and hashcode of x is:",hex(id(x)))
print("y is:",y,"and hashcode of y is:",hex(id(y)))

for i in range(0, len(x)):
    y[i] = y[i]*2

for i in range(0, len(x)):
   print(x[i], end="  ")

print()

print("x is:",x,"and hashcode of x is:",hex(id(x)))
print("y is:",y,"and hashcode of y is:",hex(id(y)))

print("This is how we use \nbackslash n")


# Create a function which takes input as list
# it will convert the elements with squares
# def squares(numbers):
#     .....
#
# data = [1, 3, 5, 7, 9]
# square(data)
# print(data)


