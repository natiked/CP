word = input()
woLis = list(word)
lower = 0
upper = 0
for wo in woLis:
    if wo > "Z":
        lower += 1
    else:
        upper += 1

if upper > lower:
    print(word.upper())
else:
    print(word.lower())
