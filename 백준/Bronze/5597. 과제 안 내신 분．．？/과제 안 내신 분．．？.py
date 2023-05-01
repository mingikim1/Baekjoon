import sys

okay = []

for i in range(28) :
    okay.append(int(sys.stdin.readline()))

okay = set(okay)

all = []

for i in range(30) :
    all.append(i+1)

all = set(all)

no = list(all - okay)
no.sort()

for i in no :
    print(i)
