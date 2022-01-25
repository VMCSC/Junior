maxWeight = int(input())
numItems = int(input())
items = [[int(j) for j in input().split()] for i in range(numItems)]
knapsack = [0 for i in range(maxWeight + 1)]
for i in range(maxWeight + 1):
    for j in items:
        if j[1] >= i:
            knapsack[i] = max(knapsack[i], knapsack[i-j[1]] + j[0])
print(knapsack[maxWeight])