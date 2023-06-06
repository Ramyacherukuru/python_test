students = []
while True:
    student = input("Enter the name and marks of the student:")
    if student =='':
        break
    name,marks = student.strip().split(',')
    students.append((name,int(marks)))

s = sorted(students,  key = lambda  x:x[1])
print("students who scores more than 90:")

for student in s:
    if student[1] > 90:
        print(student)










































