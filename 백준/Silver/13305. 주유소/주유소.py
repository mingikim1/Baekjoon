import sys

input = sys.stdin.readline

N = int(input())

l = list(map(int , input().split()))
o = list(map(int , input().split()))

a1 = o[0]
result = 0

for i in range(N-1) :
    if a1 < o[i] :
        result += a1 * l[i]
    else :
        a1 = o[i]
        result += a1 * l[i]

print(result)
