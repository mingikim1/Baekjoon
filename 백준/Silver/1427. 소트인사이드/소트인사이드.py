N = input()

num_array = []

for i in range(len(N)) :
    num_array.append(int(N[i]))

num_array.sort(reverse = True)

for i in range(len(num_array)) :
    num_array[i] = str(num_array[i])

print(''.join(num_array))