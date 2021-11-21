def anagram(letters,anagramWord = ""):
    if len(letters) == 0:
        print(anagramWord)
        return
    for i in range(len(letters)):
        anagram(letters[:i] + letters[i+1:], anagramWord + letters[i])
anagram(sorted(input()))