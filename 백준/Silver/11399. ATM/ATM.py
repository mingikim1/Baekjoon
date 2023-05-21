import sys

input = sys.stdin.readline

N = int(input())

P = list(map(int, input().split()))

P.sort()

S = 0
Su = []

for i in range(N) :
    S += P[i]
    Su.append(S)

print(sum(Su))