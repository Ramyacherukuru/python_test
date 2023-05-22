FH = open("story_S10Q01.txt",'r')
all_text = FH.read()
all_lines = all_text.strip().split('\n')
print(all_lines)
FH.close()


FH1 = open("story1_S10Q01.txt",'w')
for line in all_lines:
    
    FH1.write(line)
    FH1.write('\n')

    
FH1.close()

