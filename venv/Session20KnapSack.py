itemValue = [4000, 3500, 1800, 400, 1000, 200]
itemWeights = [20, 10, 9, 4, 2, 1]


import itertools
N = 6
combinations = list(itertools.product([0, 1], repeat=N))

items = []
coms = []

for com in combinations:

    sum1 = 0
    sum2 = 0
    for i in range(0, len(com)):
        print(com[i], end=" ")

        if com[i] is 1:
            sum1 = sum1 + itemValue[i]
            sum2 = sum2 + itemWeights[i]

    if sum2 <= 20:
        items.append(sum1)
        coms.append(com)

    print()

print(items)
print(coms)