n = int(input())
arr = [int(i) for i in input().split()]
longestOverall = 1
dp = [1 for i in range(n)]
for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])
    longestOverall = max(longestOverall, dp[i])
print(longestOverall)