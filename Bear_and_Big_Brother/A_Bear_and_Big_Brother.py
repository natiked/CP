weight = input()
weightList = weight.split()
weightL = int(weightList[0])
weightB = int(weightList[1])
year = 0
while weightL <= weightB:
    weightB *= 2
    weightL *= 3
    year += 1

print(year)
