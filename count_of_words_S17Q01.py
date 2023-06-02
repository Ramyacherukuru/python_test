word_count = {}

with open("count_S17Q01.txt", 'r') as FH:
    line = FH.read()

words = line.split()

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

print("Top 10 most repeated words:")
for word, count in sorted_words:
    print(word ,":", count)

non_repeated_words = [word for word, count in sorted_words if count == 1]
print("Words that are not repeated:", ",".join(non_repeated_words))
       
        
