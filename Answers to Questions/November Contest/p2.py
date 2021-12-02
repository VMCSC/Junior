input()
word = input()
sum = 0
for i in range(1, len(word)):
    sum += abs(ord(word[i]) - ord(word[i-1]))
print(sum)