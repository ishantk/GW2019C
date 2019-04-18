a = 10

def show():
    global a # We have a in the main
    a = 20

    print("a in show is:",a)


show()
print("a is:",a)