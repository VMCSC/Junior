def patternGen(maxLength, maxBits, curBits=0, string=""):
    if len(string) == maxLength:
        print(string)
        return
    if curBits < maxBits:
        patternGen(maxLength, maxBits, curBits + 1, string+"1")
    if maxBits - curBits != maxLength - len(string):
        patternGen(maxLength, maxBits, curBits, string+"0")
numPat = int(input())
for i in range(numPat):
    n, k = [int(i) for i in input().split()]
    print("The bit patterns are")
    patternGen(n, k)