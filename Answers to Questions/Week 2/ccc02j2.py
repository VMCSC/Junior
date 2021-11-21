vowel = "aeiouy"
while True:
    word = input()
    if word == "quit!":
        break
    if len(word) <= 4:
        print(word)
        continue
    if word[-2:] == "or" and vowel.find(word[-3]) == -1:
        print(word[:-2] + "our")
    else:
        print(word)