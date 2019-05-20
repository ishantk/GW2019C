a = 10 # Global Variable

entryID = None

def hello():
    global entryID
    # global a
    a = 12 # Creating a local variable a for function hello
    print("a is:",a)
    print(entryID)

hello()

print("a is:",a)


data = "John loves to play cricket"

if data.__contains__("cricket") or data.__contains__("play"):
    print("Cricket is in the data")


b = 10
skills = [10, 20, 30, 40, 50]
for i in range(0, len(skills)):
    print("found")




