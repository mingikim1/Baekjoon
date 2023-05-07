import sys

grade_dic = {'A+' : 4.5 , 'A0' : 4.0 , 'B+' : 3.5 , 'B0' : 3.0 , 'C+' : 2.5 , 'C0' : 2.0 , 'D+' : 1.5 , 'D0' : 1.0 , 'F' : 0.0}

grade_all = []
credit_all = []

for i in range(20) :
    subject , credit , grade = sys.stdin.readline().split()
    credit = float(credit)
    if grade == 'P' :
        continue
    grade_all.append(credit*grade_dic[grade])
    credit_all.append(credit)

print(sum(grade_all)/sum(credit_all))