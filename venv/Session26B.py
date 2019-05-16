print(">> App Started")

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = 0
try:
    num3 = num1 / num2
except ZeroDivisionError as zRef:
    print(">> Error: ",zRef)

print(">> Result is:",num3)

print(">> App Finished")