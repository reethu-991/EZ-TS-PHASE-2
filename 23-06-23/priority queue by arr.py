'''append eles(key,value)
key : priority
value: ele in queue and sort the list every time an ele is append'''
stu_grade=[]
stu_grade.append((1,'a'))
stu_grade.append((4,'d'))
stu_grade.sort(reverse=True)
print('yes')
print(stu_grade)

stu_grade.append((3,'c'))
stu_grade.sort(reverse=True)
stu_grade.append((2,'b'))

stu_grade.sort(reverse=True)
print('priority wise')
print(stu_grade)

print('original queue')
while stu_grade:
    print(stu_grade.pop())
    
