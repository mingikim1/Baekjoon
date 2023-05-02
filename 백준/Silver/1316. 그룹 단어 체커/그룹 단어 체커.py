import sys

N = int(input())
num_array = []
counting = 0
for i in range(N) :
    S = sys.stdin.readline().strip()
    S_set = set(S)
    for j in S_set :
        num_array = []
        for k in range(len(S)) :
            if S[k] == j :                
                num_array.append(k)
                conti = True
                if len(num_array) == 1 :
                    continue
        for l in range(len(num_array) - 1) :
            if num_array[l+1]-num_array[l] != 1 :
                conti = False
                break
        if conti == False :
            break
    if conti == True :
        counting = counting + 1

print(counting)