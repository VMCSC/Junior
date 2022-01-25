totalMoney = int(input())
numCoins = int(input())
coins = [int(i) for i in input().split()]
dollars = [999999999999999 for i in range(totalMoney + 1)]
dollars[0] = 0

for i in coins:
    for j in range(i, totalMoney + 1):
        dollars[j] = min(dollars[j], dollars[j-i] + 1)

print(dollars[totalMoney])