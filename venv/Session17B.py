# Inheritance
"""
    Single Level
    A
    |
    B

    class A:
        pass

    class B(A):
        pass

    Multi Level
    A
    |
    B
    |
    C

    Hierarchy
    A
    |
  B   C

    Multiple
  A   B
    |
    C

  class A:
    pass

  class B:
    pass

  class C(A, B)
    pass

  Hybrid
    Any Combination Above

"""

class A:

    x = 10

    def show(self):
        print(">> show of A")

class B:

    x = 20

    def show(self):
        print(">> show of B")

    def hello(self):
        print(">> This is hello from B")

class C(B, A):

    x = 30

    pass

cRef = C()
cRef.x = 100

cRef.show()
cRef.hello()

print(cRef.x)
print(C.x)