board = [input() for i in range(3)]
x = False
o = False
if board[0][0] == board[1][1] == board[2][2]:
    if board[1][1] == 'X':
        x = True
    else:
        o = True
if board[2][0] == board[1][1] == board[0][2]:
    if board[1][1] == 'X':
        x = True
    else:
        o = True
for i in range(3):
    if board[0][i] == board[1][i] == board[2][i]:
        if board[0][i] == 'X':
            x = True
        else:
            o = True
    if board[i][0] == board[i][1] == board[i][2]:
        if board[i][0] == 'X':
            x = True
        else:
            o = True
if x and o:
    print("Error, redo")
elif x:
    print("Timothy")
elif o:
    print("Griffy")
else:
    print("Tie")