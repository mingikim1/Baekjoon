
ex = input().split("-")


for i in range(len(ex)) :
    ex[i] = ex[i].split("+")

if ex[0] == [''] :
    result = 0
    for i in range(len(ex) - 1) :
        s = 0
        for j in range(len(ex[i+1])) :
            s += int(ex[i+1][j])
        result -= s
    print(result)

else:
    result_l = []
    for i in range(len(ex)) :
        s = 0
        for j in range(len(ex[i])) :
            s += int(ex[i][j])
        result_l.append(s)
    result = result_l[0]
    for i in range(len(result_l)-1) :
        result -= result_l[i+1]
    print(result)
