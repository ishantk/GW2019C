n1 = 10
n2 = 20

print("Is n1 greater than n2 ? ",n1>n2)

# Conditional Constructs (if/else)
if n1 > n2:
    print(n1,"is greater than",n2)
else:
    print(n2, "is greater than", n1)

billingAmount = 1000
promoDiscount = 50 # Condition : >=500

if billingAmount >= 500:
    billingAmount = billingAmount // 2
    print("Please Pay \u20b9",billingAmount)
else:
    print("Please Pay \u20b9", billingAmount)


print()

# Nested if/else
isInternetEnabled = False
isGPSEnabled = False

if isInternetEnabled:
    if isGPSEnabled:
        print("You can browse Google Maps")
    else:
        print("Please Enable GPS and Try Again !!")
else:
    print("Please Enable Internet and Try Again !!")

print()

if isInternetEnabled and isGPSEnabled:
    print("You can browse Google Maps")
else:
    print("Please Enable Internet or GPS and Try Again !!")

# Ladder if/else
physics = 90
maths = 87
chemistry = 80

marksAverage = (physics + maths + chemistry)//3

if marksAverage >=80:
    print("Grade A Awarded for Securing",marksAverage)
elif marksAverage >=70 and marksAverage <80:
    print("Grade B Awarded for Securing", marksAverage)
elif marksAverage >=60 and marksAverage <70:
    print("Grade C Awarded for Securing", marksAverage)
elif marksAverage >= 50 and marksAverage < 60:
    print("Grade D Awarded for Securing", marksAverage)
else:
    print("Grade E Awarded for Securing", marksAverage)
