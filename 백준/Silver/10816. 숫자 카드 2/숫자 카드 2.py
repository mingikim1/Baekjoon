import sys

input = sys.stdin.readline

N = int(input())

X = list(map(int , input().split()))

M = int(input())

Y = list(map(int , input().split()))

Y_dic = {}

for i in X :
    if i in Y_dic :
        Y_dic[i] += 1
    else :
        Y_dic[i] = 1

for i in Y :
    if i in Y_dic :
        print(Y_dic[i] , end = ' ')
    else :
        print(0 , end = ' ')