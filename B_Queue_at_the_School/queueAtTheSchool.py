nAndT = (input().split())
queue = list(input())

timer = int(nAndT[1])
i = 0
swap = []
while timer > 0:
    swap = []
    for j in range(len(queue)-1):
        if queue[j] == "B" and queue[j+1] == "G":
            swap.append(j)
    for i in swap:
        queue[i], queue[i+1] = queue[i+1], queue[i]
    timer -= 1

print("".join(queue))

