img = []
with open("input.in", "r") as file:
    x = list(map(int, file.readline().split()))
    for i in range(x[0]):
        img.append(str(file.readline().strip()))

complete = []

for i in range(x[0]):
    for k in range(x[2]):
        y = []
        m = 0
        for j in img[i]:
            y.append(img[i][m] * x[2]) 
            m += 1
        complete.append("".join(y))
    

with open("output.out", "w") as file:
    for i in range(x[0]*x[2]):
        file.writelines(complete[i] + "\n")

    

        

        
