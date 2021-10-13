n = int(input())
grid = [[int(j) for j in input().split()] for i in range(n)]
tL = grid[0][0]
tR = grid[0][n-1]
bL = grid[n-1][0]
bR = grid[n-1][n-1]

if tL < tR and tL < bL and tL < bR:
    for i in grid:
        for j in range(n-1):
            print(i[j], end =" ")
        print(i[n-1])
elif tR < tL and tR < bL and tR < bR:
    for i in range(n):
        for j in range(n-1):
            print(grid[j][n-i-1], end=" ")
        print(grid[n-1][n-i-1])
elif bR < tL and bR < tR and bR < bL:
    for i in range(n):
        for j in range(n-1):
            print(grid[n-i-1][n-j-1], end=" ")
        print(grid[n-i-1][0])
else:
    for i in range(n):
        for j in range(n-1):
            print(grid[n-j-1][i], end=" ")
        print(grid[0][i])