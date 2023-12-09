A, B = map(int, input().split())

count = 1

while(True) :
    if B%2 == 0 :
        B = B/2
        count += 1
        
    else :
        B = (B-1)/10
        count += 1
        
    if A == B :
        break
    
    if A > B :
        count = -1
        break

print(count)