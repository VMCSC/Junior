antonia = 100
david = 100
n = int(input())
for i in range(n):
    antoniaRoll, davidRoll = [int(i) for i in input().split()]
    if antoniaRoll > davidRoll:
        david -= antoniaRoll
    elif davidRoll > antoniaRoll:
        antonia -= davidRoll

print(antonia)
print(david)