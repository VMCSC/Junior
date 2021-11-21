magicSquare = [[int(k) for k in input().split()] for i in range(4)]
sumofsquare = magicSquare[0][0] + magicSquare[0][1] + magicSquare[0][2] + magicSquare[0][3]
valid = True
for i in range(4):
    if sumofsquare != magicSquare[i][0] + magicSquare[i][1] + magicSquare[i][2] + magicSquare[i][3]:
        valid = False
    if sumofsquare != magicSquare[0][i] + magicSquare[1][i] + magicSquare[2][i] + magicSquare[3][i]:
        valid = False

if valid:
    print("magic")
else:
    print("not magic")