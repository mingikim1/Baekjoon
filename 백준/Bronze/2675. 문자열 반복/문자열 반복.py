T = int(input())

num = []
alpha = []

for i in range(T) :
    R , S = input().split()
    R  = int(R)
    for j in S :
        print(j * R , end = '')
    print()