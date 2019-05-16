# User Defined Exception
class BankingException(Exception):
    pass

accBalance = 10000
minBalance = 2000
attempts = 0

def withdraw(amount):
    global accBalance
    global minBalance
    global attempts

    accBalance = accBalance - amount

    if accBalance <= minBalance:
        print(">> Balance is LOW!! You cannot Withdraw !!")
        attempts = attempts + 1
    else:
        print(">> Withdraw Success and new Balance is: \u20b9",accBalance)


    if attempts == 3:
        # error = ZeroDivisionError("Illegal Attempts")
        error = BankingException("Illegal Attempts")
        raise error

print(">> App Started")

for i in range(0,100):
    withdraw(3000)

print(">> App Finished")