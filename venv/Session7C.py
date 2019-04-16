a = 10

def fun():
    b = 10
    print("This is fun and b is:",b)

print("HashCode of a is:",id(a))
print("HashCode of a in hex is:",hex(id(a)))

print("HashCode of fun is:",id(fun))
print("HashCode of fun in hex is:",hex(id(fun)))
print("fun is:",fun)

fun()

# Reference Copy
abc = fun

print("abc is:",abc)
abc()

"""
    Create a function with any name to solve below problem:
    Input to function will be number of bricks
    and output will be who placed the last brick
    
    def createWall(bricks):
        .
        ..
        ...
        
        return "jack"
        
    
    Problem:
    Ask for number of bricks
    N = 7
    
    john    1, 2, 3, 4, 5, 6, 7, .....
    jack    2, 4, 6, 8, 10, 12, 14 .....

    john    1     6
    jack    2     4
    john    2     2
    jack    2/4   0     

    Loops and if/else | break
    
    30 - 40 mins

"""