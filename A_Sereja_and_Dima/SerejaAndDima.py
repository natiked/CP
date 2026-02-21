n = int(input())
numbers = input()
numsLis = numbers.split()
left = 0
right = -1
s = 0
d = 0
whoseTurn = 0
count = 1

while count<=n:
    if int(numsLis[left]) > int(numsLis[right]):
        if whoseTurn == 0:
            s += int(numsLis[left])
            whoseTurn = 1
        else:
            d += int(numsLis[left])
            whoseTurn = 0
        left += 1
    else:
        if whoseTurn == 0:
            s += int(numsLis[right])
            whoseTurn = 1
        else:
            d += int(numsLis[right])
            whoseTurn = 0
        right -= 1
    count += 1
print(f"{s} {d}")


