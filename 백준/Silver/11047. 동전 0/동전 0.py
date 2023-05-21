import sys

input = sys.stdin.readline

N , K = map(int , input().split())

V = []

for i in range(N) :
    V.append(int(input()))

V_l = len(V) - 1

S = []

while (V_l >= 0) :
    m = int(K/V[V_l])
    if m >= 1 :
        S.append(m)
        K = K - V[V_l] * m
        if K == 0 :
            break
    V_l -= 1

print(sum(S))