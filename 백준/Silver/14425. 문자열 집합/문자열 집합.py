N , M = input().split()
N = int(N)
M = int(M)

S = []
U = []

for i in range(N) :
    S.append(input())
      
for i in range(M) :
    U.append(input())
    
S = set(S)

count = 0
for i in range(M) :
    if U[i] in S :
        count = count + 1
        
print(count)