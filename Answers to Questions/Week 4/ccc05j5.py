def monkey(stringInput):
    if stringInput == "":
        return False
    if stringInput == "A":
        return True
    for i in range(1, len(stringInput)):
        if stringInput[i] == "N" and monkey(stringInput[:i]) and monkey(stringInput[i+1:]):
            return True
    if stringInput[0] == "B" and stringInput[-1] == "S":
        return monkey(stringInput[1:-1])
    return False
while True:
    stringInput = input()
    if stringInput == "X":
        break
    if monkey(stringInput):
        print("YES")
    else:
        print("NO")