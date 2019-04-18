
count = 1

def increment():
    global count
    count = count + 1

def decrement():
    global count
    count = count - 1

def double():
    global count
    count = count * 2

def modulo():
    global count
    count = count % 2

def wow():
    count = 12

increment() #2
double()    #4
modulo()    #0
increment() #1
decrement() #0
wow()

print("count is:", count)