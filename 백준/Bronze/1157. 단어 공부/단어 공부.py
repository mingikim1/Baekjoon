alphabet = input()

alphabet = list(alphabet.upper())

set_alphabet = list(set(alphabet))

set_len = len(set_alphabet)

counting = []

for i in range(set_len) :
    counting.append(alphabet.count(set_alphabet[i]))
    
max_num = max(counting)

if counting.count(max_num) != 1 :
    print("?")

else :
    print(set_alphabet[counting.index(max(counting))])
    