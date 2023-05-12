N = int(input())

cr = []

for i in range(N) :
    age , name = input().split()
    age = int(age)
    cr.append([age , name])
    
cr.sort(key = lambda x : (x[0]))

for i in range(len(cr)) :
    print(cr[i][0] , cr[i][1] , sep = ' ')