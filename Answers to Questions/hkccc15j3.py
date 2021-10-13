import pprint
n, m = [int(i) for i in input().split()]
board = [[False for x in range(n)] for y in range(n)]
for i in range(m):
    x, y = [int(i) for i in input().split()]
    x -= 1
    y -= 1
    for j in range(n):
        board[x][j] = True
        board[j][y] = True
        if 0 <= x + (y - j) < n:
            board[x + (y-j)][j] = True
        if 0 <= x - (y - j) < n:
            board[x - (y-j)][j] = True
            
notMovable = 0
for i in board:
    for j in i:
        if not j:
            notMovable += 1

print(notMovable)