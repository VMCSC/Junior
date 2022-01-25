x = input()
y = input()
dp = [[-1 for j in range(len(y)+1)] for i in range(len(x)+1)]
for i in range(len(x) + 1):
    for j in range(len(y) + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif x[i-1] == y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else: 
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len(x)][len(y)])