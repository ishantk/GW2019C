#  *args -> Receives data as tuple
def fun(*args): # args -> arguments / inputs
    print(args)
    print(type(args))
    print()

fun(10, 20)
fun(10, 20, 30)
fun(10, 20, 30, 'A')
fun(10, 20.22, 30, 'A', 2.2)

#  **kwargs -> Receives data as dictionary
def show(**kwargs): # kwargs -> keyword arguments / inputs
    print(args)
    print(type(args))

    # Do some stuff where you can increment the salary by 10percent

    print()



show(name="John", age = 20, salary=30000)
show(name="Fionna", age = 22, salary=40000)

