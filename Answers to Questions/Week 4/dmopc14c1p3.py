I = int(input())
markSum = 0
for i in range(I):
    markSum += int(input())
S = int(input())
for i in range(S):
    markSum += int(input())
    print("%.3f" % (markSum/(I+i+1)))