import sys
input = sys.stdin.readline

S = input().rstrip()
S_sub = []
for i in range(1,len(S)+1) :
    for j in range(len(S)-i+1) :
        S_sub.append(S[j:j+i])

print(len(set(S_sub)))