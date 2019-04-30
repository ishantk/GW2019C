class Counter:

    # Property of Class
    count1 = 1

    def __init__(self):
        self.count2 = 1 # Property of Object


c1 = Counter()
c1.a = 10

c2 = Counter()
c2.a = 12

Counter.x = 10

print(c1.__dict__)
print(Counter.__dict__)