import sys

input = sys.stdin.readline

N = int(input())

X = list(map(int , input().split()))

X_sorted = sorted(list(set(X)))

dic_X = {}

for i in range(len(X_sorted)) :
    dic_X[X_sorted[i]] = i

for i in range(len(X)) :
    print(dic_X[X[i]] , end = ' ')