maxWeight = int(input())
numItems = int(input())
items = [[int(j) for j in input().split()] for i in range(numItems)]
knapsack = [[0 for j in range(maxWeight + 1)] for i in range(numItems + 1)]
for i in range(numItems):
    for j in range(maxWeight + 1):
        knapsack[i+1][j] = knapsack[i][j]
        if j >= items[i][1]:
            knapsack[i+1][j] = max(knapsack[i+1][j], knapsack[i][j-items[i][1]] + items[i][0])
print(knapsack[numItems][maxWeight])