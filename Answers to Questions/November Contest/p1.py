a, b = [int(i) for i in input().split()]
while True:
    if a % b != 0:
        print("No")
        break
    if a == b:
        print("Yes")
        break
    a /= b