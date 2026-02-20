n = int(input())

probSolved = 0
for i in range(n):
    count = 0
    vot = input()
    z = list(vot)
    for j in z:
        try:
            count += int(j)
        except:
            continue
    if count>= 2:
        probSolved += 1
        
print(probSolved)

