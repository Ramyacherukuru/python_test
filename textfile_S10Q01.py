filename = input("Enter the name of the text file: ")
FH = open(filename,'r')
all_text = FH.read()
all_lines = all_text.split('.')
print(all_lines)
all_sent = []
for line in all_lines:
    if (line.strip()[0].isupper()):
        all_sent.append(True)
        
    else:
        all_sent.append(False)
for val in all_sent:
    if val == True:
        continue
    else:
        print("bad sentence")

        
print("Done")
