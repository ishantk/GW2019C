def checkNumber(num):
    return True

def filterNumbers(numbers):
    for i in range(0, len(numbers)):

        if checkNumber(numbers[i]):
            numbers[i] = 1
        else:
            numbers[i] = 0

data = [121, 235, 545, 555, 789]
filterNumbers(data)
print(data) # [1, 0, 1, 1, 0]