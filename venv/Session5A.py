# Loops
n = int(input("Enter n: "))
for i in range(1, n+1): # begin form 1 but less than 11

    if i%2 == 0:
        print("Even:",i)
    else:
        print("Odd:",i)

print("Sum of Odd Numbers is: ")
print("Sum of Even Numbers is: ")

print()
num = int(input("Enter Number: "))

# for i in range(1, 21):
for i in range(1, 21, 2):
    print(num,i,"'s are",(num*i))

# Challenege:
# 1 2 3 4 5 6 7 8 9 10 ...... n
# 1 + 3 + 5 + ....
# 2 + 4 + 6 + ....