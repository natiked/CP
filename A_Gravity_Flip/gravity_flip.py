n = int(input())
ord = input()
lis = ord.split()

for i in range(n):
    for j in range(i+1, n):
        if int(lis[i]) > int(lis[j]):
            lis[i], lis[j] = lis[j], lis[i]

print(" ".join(lis))
