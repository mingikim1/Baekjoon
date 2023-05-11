N = int(input())

li = []

for i in range(N) :
    [x , y] = map(int , input().split())
    li.append([x , y])

li.sort()

for i in range(N) :
    print(li[i][0] , li[i][1] , sep = ' ')