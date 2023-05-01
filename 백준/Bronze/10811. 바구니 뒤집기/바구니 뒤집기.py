import sys

N , M = map(int , sys.stdin.readline().split())

basket = []

for k in range(N) :
    basket.append(k+1) 

for k in range(M) :
    i , j = map(int , sys.stdin.readline().split())
    r_b = basket[i-1:j]
    r_b.reverse()
    basket[i-1:j] = r_b
    
for i in basket :
    print(i , end = ' ')