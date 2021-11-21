for n in range(5):
    board = [input() for i in range(3)]
    x = False
    o = False
    if board[0][0] == board[1][1] == board[2][2]:
        if board[1][1] == 'X':
            x = True
        elif board[1][1] == 'O':
            o = True
    if board[2][0] == board[1][1] == board[0][2]:
        if board[1][1] == 'X':
            x = True
        elif board[1][1] == 'O':
            o = True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                x = True
            elif board[0][i] == 'O':
                o = True
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                x = True
            elif board[i][0] == 'O':
                o = True
    if x:
        print("X")
    elif o:
        print("O")
    else:
        print(".")
