N = int(input())

X = set(map(int , input().split()))

M = int(input())

Y = list(map(int , input().split()))

W = set(Y)

Z = W - X

for i in range(M) :
    if Y[i] in Z :
        Y[i] = 0
    else : Y[i] = 1

for i in range(M) :
    print(Y[i] , end = ' ')
