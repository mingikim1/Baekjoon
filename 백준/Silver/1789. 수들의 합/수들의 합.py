import sys

input = sys.stdin.readline

S = int(input())

c = 0
i = 1

while (S >= 0) :
    S = S - i
    c += 1
    i += 1

print(c-1)