word = input()
validLetters = "IOSHZXN"
invalid = False
for i in word:
    if not i in validLetters:
        invalid = True
if invalid:
    print("NO")
else:
    print("YES")