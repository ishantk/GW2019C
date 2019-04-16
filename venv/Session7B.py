# Takes no input and is returning nothing
def areaOfRectangle():

    length = int(input("Enter Length: "))
    breadth = int(input("Enter Breadth: "))

    area =  length * breadth

    print("Area is:", area)


ans = "yes"

while ans == "yes":

    # Execution
    areaOfRectangle()
    ans = input("Wish to calculate more Area? (yes/no)")
