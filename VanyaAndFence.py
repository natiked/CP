nh = input()
height = input()
nhLis = nh.split()
heightLis = height.split()
hmax = int(nhLis[1])
width = 0
for i in heightLis:
    if int(i) > hmax:
        width += 2
    else:
        width += 1
print(width)
