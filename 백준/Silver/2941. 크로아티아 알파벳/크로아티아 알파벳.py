C = ['c=' , 'c-' , 'dz=' , 'd-' , 'lj' , 'nj' , 's=' , 'z=']

alpha = input()

for i in C :
    alpha = alpha.replace(i , '*')

print(len(alpha))