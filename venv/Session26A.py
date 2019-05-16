print(">> Python App Started")

numbers = [10, 20, 30, 40, 50]
# Exception Handling
try:
    print("numbers[30] is:",numbers[30])
# except IndexError as iRef:
except Exception as e:
    print("Some Error !!", e)
finally:
    print("This will be definitely executed")

print(">> Python App Finished")