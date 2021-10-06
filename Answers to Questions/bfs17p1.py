n = input()
hobbies = input().split()
hobbiesWritten = 0
for i in hobbies:
    if len(i) <= 10:
        hobbiesWritten += 1

print(hobbiesWritten)