n = int(input())
villages = [int(input()) for i in range(n)]
villages.sort()
max2Size = 2000000001
for i in range(1, n-1):
    max2Size = min(max2Size, villages[i+1] - villages[i-1])
print("%.1f" % (max2Size/2))