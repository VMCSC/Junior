w = int(input())
h = int(input())

for i in range(h):
    for j in range(w):
        if i % 2 == j % 2:
            print("0", end='')
        else:
            print("1", end='')
    print()