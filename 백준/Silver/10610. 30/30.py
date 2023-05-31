import sys

input = sys.stdin.readline

n = int(input())

N_list = list(map(int ,str(n)))

if 0 not in N_list :
    print(-1)

else :
    s = 0
    for i in range(len(N_list)) :
        s += N_list[i]
    if s % 3 == 0 :
        N_list.sort(reverse = True)
        for j in range(len(N_list)) :
            print(N_list[j] , end = '')
    else :
        print(-1)
