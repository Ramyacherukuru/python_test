FH = open("story_S10Q01.txt",'r')
all_lines = FH.read()
print(all_lines)
search_word = input("Enter the word you want to search:")
replace_word = input("Enter the word you want to replace it with:")

if search_word in all_lines:
    print("Search success")
else:
    print("search unsuccess")

modified_content = all_lines.replace(search_word, replace_word)
print(modified_content)

