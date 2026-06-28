n = int(input())
m = abs(n)
l = list(map(int, str(m)))

if n < 0:
    if l[-1] > l[-2]:
        l.pop()
        if l[0] == 0:
            print("".join(list(map(str, l))))
        else:
            print("-" + "".join(list(map(str, l))))
    else:
        l.pop(-2)
        if l[0] == 0:
            print("".join(list(map(str, l))))
        else:
            print("-" + "".join(list(map(str, l))))
else:
    print(n)




