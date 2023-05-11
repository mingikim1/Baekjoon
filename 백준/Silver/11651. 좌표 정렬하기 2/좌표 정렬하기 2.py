N = int(input())

li = []

for i in range(N) :
    [x , y] = map(int , input().split())
    li.append([y , x])

li.sort()

for i in range(N) :
    print(li[i][1] , li[i][0] , sep = ' ')