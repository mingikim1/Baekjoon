A_array = []

for i in range(10) :
    A_array.append(int(input()))

count = 10

for i in range(10) :
    A_array[i] = A_array[i]%42
    
A_array.sort()

for i in range(9) :
    if A_array[i] == A_array[i+1] :
        count = count - 1
        
print(count)