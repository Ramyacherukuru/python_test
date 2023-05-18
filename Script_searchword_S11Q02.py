FH = open("story_S10Q01.txt",'r')
all_text = FH.read()
all_lines = all_text.split('\n')
print(all_lines)

search_word = input("Enter the word to be search:")
for line in all_lines:
    if search_word in line:
        print(line)
