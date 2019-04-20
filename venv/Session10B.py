# Default Arguments
def area(l=10, b=5):
    return l * b

x = int(input("Enter Length: "))
y = int(input("Enter Breadth: "))

print("Area is: ",area(x))
print("Area is: ",area(y))
print("Area is: ",area())


print("Area is: ",area(l=x))
print("Area is: ",area(b=y))
print("Area is: ",area())
print("Area is: ",area(l=x, b=y))
