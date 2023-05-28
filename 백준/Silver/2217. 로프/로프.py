import sys

input = sys.stdin.readline

N = int(input())

n_arr = []

for i in range(N) :
    n_arr.append(int(input()))

n_arr.sort()

result = []

for i in range(N) :
    result.append((N-i)*n_arr[i])

print(max(result))