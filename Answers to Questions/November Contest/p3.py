n, m = [int(i) for i in input().split()]
matrix = [[int(j) for j in input().split()] for i in range(n)]
t = int(input())
if t % 2 == 0:
    for i in range(n):
        for j in range(m - 1):
            print(matrix[i][j], end=" ")
        print(matrix[i][m - 1])
else:
    for i in range(m):
        for j in range(n - 1):
            print(matrix[j][i], end=" ")
        print(matrix[n-1][i])
