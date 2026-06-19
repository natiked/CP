n = int(input())
order = list(map(int, input().split()))

c = 1
cmax = 1

for i in range(1, n):
    x = order[i-1]

    if x <= order[i]:
        c += 1

    else: 
        if c > cmax:
            cmax = c
        c = 1

print(max(c, cmax))

