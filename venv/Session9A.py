def squares(numbers):
    for i in range(0, len(numbers)):
        numbers[i] = numbers[i] * numbers[i]

data = [1, 3, 5, 7, 9]
squares(data) # Pass By Reference
print(data)