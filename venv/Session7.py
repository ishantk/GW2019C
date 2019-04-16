"""
    What is a function ?
    Which will do some Task !!
    It will take an input/inputs and process it to provide some result
    f(x)

    f(length, breadth) = length * breadth
    f1(temp) = temp + 1
    f2(temp) = temp - 1

"""

# Definition (Creating Function)        |       Modularization
def areaOfRectangle(length, breadth):
    return length * breadth

def increaseTemp(temp):
    return temp + 1


ans = "yes"

while ans == "yes":
    length = int(input("Enter Length: "))
    breadth = int(input("Enter Breadth: "))
    print("Area is:", areaOfRectangle(length, breadth) ) # Execution

    ans = input("Wish to calculate more Area? (yes/no)")


print("New Temperature is:",increaseTemp(5))