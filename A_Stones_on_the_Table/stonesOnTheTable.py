n = int(input())
colors = input()

move = 0
start = 0
lastletter = colors[0]
for i in colors:
    if start == 0:
        start = 1
    else:
        if i == lastletter:
            move += 1
            lastletter = i
        else:
            lastletter = i

print(move)
