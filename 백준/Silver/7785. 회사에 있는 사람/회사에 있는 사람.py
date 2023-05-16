import sys
input = sys.stdin.readline

N = int(input())

log = {}

for i in range(N) :
    name , el = input().split()
    log[name] = el    
    if log[name] == 'leave' :
        del log[name]

log_name = list(log.keys())

log_name.sort(reverse = True)

for i in range(len(log_name)) :
    print(log_name[i])