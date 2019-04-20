"""
def addNumbers(num1, num2):
    result = num1 + num2
    return result

print("addNumbers is:",addNumbers)

def addNumbers(num1, num2, num3):
    result = num1 + num2 + num3
    return result

print("addNumbers now is:",addNumbers)

"""

"""
def addNumbers1(num1, num2):
    result = num1 + num2
    return result

def addNumbers2(num1, num2, num3):
    result = num1 + num2 + num3
    return result
    
"""

# Input with * will take n number of values and make a tuple out of it
def addNumbers(*numbers):
    # print(numbers)
    # print(type(numbers))

    sum = 0;
    for i in range(0, len(numbers)):

        # numbers[i] -> is this a prime or not
        
        sum = sum + numbers[i]

    return sum

a = int(input("Enter a number:"))

print("Addition is: ",addNumbers(a,20))
print("Addition is: ",addNumbers(10, 20, 30))
print("Addition is: ",addNumbers(10, 20, 30, 40, 50))
print("Addition is: ",addNumbers(1, 3, 2, 5, 6, 9, 7, 11))
