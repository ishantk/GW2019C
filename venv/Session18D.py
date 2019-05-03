# Q. How many expressions exist in below function ?
# A. 1 : area = 3.14 * radius * radius
def areaOfCircle(radius=5):
    area = 3.14 * radius * radius
    return area

print("Area of Circle is: ",areaOfCircle())
print("Area of Circle with radius 7 is: ",areaOfCircle(7))

# Reference Copy
ac = areaOfCircle
print("Area of Circle with radius 7.5 is: ",ac(7.5))


# Lambda is an Anonymous Function | It is capable of evaluating only 1 expression
lRef1 = lambda radius=5 : 3.14 * radius * radius
print("Area of Circle with radius 9.5 is: ",lRef1(9.5))
print("Area of Circle with radius nothing is: ",lRef1())

# Create a Lambda Expression which tells number as odd or even in result
lRef2 = lambda num=0 : num%2 == 0
print("Is 5 Even?",lRef2(5))
print("Is 8 Even?",lRef2(8))

lRef3 = lambda l, b : l * b
print("Area of Rectangle with L:10 and B:12 is: ",lRef3(10, 12))

