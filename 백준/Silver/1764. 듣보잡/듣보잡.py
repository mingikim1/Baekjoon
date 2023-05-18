import sys
input = sys.stdin.readline

N , M = map(int , input().split())

xli = []
xta = []

for i in range(N) :
    xli.append(input().rstrip())

for i in range(M) :
    xta.append(input().rstrip())

xli = set(xli)
xta = set(xta)

result = list(xli&xta)
result.sort()
print(len(result))
for i in range(len(result)) :
    print(result[i])