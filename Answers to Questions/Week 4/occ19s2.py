n = int(input())
def makeNum(curNum, maxNum):
    if curNum > maxNum:
        return 0
    return makeNum(curNum * 10 + 2, maxNum) + makeNum(curNum * 10 +3, maxNum) + 1
print(makeNum(2, n) + makeNum(3, n))