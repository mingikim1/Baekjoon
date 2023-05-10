X = int(input())

line = 1

while (X > line) :
    X -= line
    line += 1

if line % 2 == 0 :
    print(X , '/' , line-X+1 , sep = '')

else :
    print(line-X+1 , '/' , X , sep = '')