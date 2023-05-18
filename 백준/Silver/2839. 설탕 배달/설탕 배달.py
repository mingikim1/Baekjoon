import sys
input = sys.stdin.readline

N = int(input())

por = int(N/5)

result = False

for i in range(por) :    
    if (N - (5 * (por-i)))%3 == 0 :
        print(int((por-i) + (N - (5 * (por-i)))/3))
        result = True
        break

if result == False :
    if N%3 == 0 :
        print(int(N/3))
    else :
        print(-1)
