def square(num):
    return num * num

lm = lambda num : num * num

numbers = [10, 11, 13, 33, 21]

# for n in numbers:
#     print(lm(n))

# result = map(square, numbers)
# Map API (Application Programming Interfaces)
result = map(lm, numbers)
print(list(result))

L1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Write a Lambda and pass it into map to tell which is even and which is odd
lm1 = lambda x : x%2 != 0
result = map(lm1 , L1)
print(list(result))



# Filter API
result = filter(lm1 , L1)
print(list(result)) # Even Numbers


lm3 = lambda P, Q : P + Q

X = [10, 20, 30, 40, 50]
Y = [11, 22, 33, 44, 55]


print("Sum of 10 and 20 is:",lm3(10, 20))
result = map(lm3, X, Y)
print(list(result))

data = [10, 20, 30, 40, 50]

from functools import reduce
result = reduce(lm3, data)
print(result)


# HW : Use Map Filter and Reduce on Dictionary !!