S = input()

num_array = []

for i in range(97,123) :
    num_array.append(-1)

for i in S :
    num_array[ord(i)-97] = S.index(i)

for i in num_array :
    print(i , end = ' ')