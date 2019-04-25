class Counter:

    def __init__(self):
        self.count = 1

    def incrementCount(self):
        self.count = self.count + 1

    def showCount(self):
        print("Count is:",self.count)


c1 = Counter()
c2 = Counter()
c3 = c1 # Reference Copy


c1.incrementCount()
c2.incrementCount()
c3.incrementCount()

c1.incrementCount()
c3.incrementCount()

c1.showCount() # Count is: 3 4
c2.showCount() # Count is: 2 2
c3.showCount() # Count is: 3 5