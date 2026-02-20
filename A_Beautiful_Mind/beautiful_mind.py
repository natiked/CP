row = []
for i in range(5):
    r = input()
    if "1" in r:
        x = i+1
        row = list(r)
y = 0
for i in row:
    try:
        if int(i) == 0:
            y +=1
        elif int(i) == 1:
            y +=1
            break
    except:
        continue

distance = abs(y-3) + abs(x - 3)
print(distance)
