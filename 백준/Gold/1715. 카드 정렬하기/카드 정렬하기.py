import sys
import heapq

input = sys.stdin.readline

N = int(input())

n_arr = []

for i in range(N) :
    heapq.heappush(n_arr , int(input()))

S = 0
if N == 1:
    print(0)

else :
    for i in range(N-1) :
        m1 = heapq.heappop(n_arr)
        m2 = heapq.heappop(n_arr)
        S += m1 + m2
        heapq.heappush(n_arr , m1 + m2)
    print(S)


