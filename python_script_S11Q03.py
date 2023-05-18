FH = open("file.txt",'r')
all_text = FH.read()
all_lines = all_text.split('\n')
print(all_lines)
FH.close()

line_no = 1
all_new_lines = []
for line in all_lines:
    if line_no % 2 == 0:
        all_new_lines.append(line)
        all_new_lines.append(line)
    else:
        all_new_lines.append(line)
        
    line_no += 1

all_new_lines.append(all_lines[0])

FH1 =open("file-new.txt",'w')
for line in all_new_lines:
    
    FH1.write(line)
    FH1.write('\n')

    
    
FH1.close()


