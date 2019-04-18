# 1. Function with no input and no output
def sayHello():
    print("This is hello from sayHello")


# 2. Function with Inputs but no output
def showGreatestNum(num1, num2):
    if num1 > num2:
        print("Greatest is:",num1)
    else:
        print("Greatest is:", num2)


# 3. Function with Inputs and output
def addNumbers(num1, num2):
    num3 = num1 + num2
    return num3
    # print("num3 is:",num3)


sayHello()
showGreatestNum(10, 20)
# result = addNumbers(11, 11)
# print("Result is:",result)
# print("Result is:",addNumbers(12,12))
result = addNumbers(10, 20)
print(result)
if result %2 == 0:
    print("Even Number")
else:
    print("Odd Number")