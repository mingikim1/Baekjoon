N = int(input())
counting = N

for i in range(N) :
    S = input()
    for j in range(len(S)-1) :
        if S[j] == S[j+1] :
            pass
        elif S[j] in S[j+1::] :
            counting += -1
            break
print(counting)