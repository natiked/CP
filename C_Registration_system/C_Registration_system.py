n = int(input())
di = {}
for i in range(n):
    word = input()
    if word in di:
        print(f"{word}{di[word]}")
        di[word] += 1
    else:
        di[word] = 1
        print("OK")
