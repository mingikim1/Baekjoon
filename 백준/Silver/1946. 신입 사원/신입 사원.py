import sys
input = sys.stdin.readline

t = int(input())

for i in range(t) :
    n = int(input())
    man = [[int(x) for x in input().split()] for _ in range(n)]
    man.sort()
    a = man[0][1]
    count = 1
    # 면접성적을 서로 비교
    for j in range(n) :
        grade = man[j][1]
        if grade < a :
            count += 1
            a = grade
    print(count)