FH = open("story_S10Q01.txt",'r')
all_text = FH.read()
all_lines = all_text.strip().split('\n')
print(all_lines)

max_e_count = 0
max_e_line = ""

for line in all_lines:
    e_count = line.count('e')
    if e_count > max_e_count:
        max_e_count = e_count
        max_e_line = line

if max_e_line:
    print("line occurence maximum no of e's :", max_e_line)
    print("count of e occurence in that line:", max_e_count)
else:
    print("No line has maximum no of e's")
