# ghadah alhoshan 443200505

grade=['A','C','A','B','B','A','C','D','C','D','E','A']

dec_grade = {}
for x in grade:
    if x in dec_grade:
        dec_grade[x]+=1
    else:
        dec_grade[x]=1
print(dec_grade)

grade_list = list(dec_grade.values())
print(grade_list)