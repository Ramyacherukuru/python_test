FH = open("Student1.txt",'r')
all_text = FH.read()
all_lines = all_text.strip().split('\n')
print(all_lines)
students = []

for line in all_lines:
    print(line)
    name,marks = line.strip().split(':')
    students.append((name,int(marks)))
s = sorted(students,  key = lambda  x:x[1])
print("students who scores more than 90:")

for student in s:
    if student[1] > 90:
        #print(student[0], student[1])
        print(*student)#tuple unpacking same as above line

























































