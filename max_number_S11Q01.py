FH = open("list_of_num_S11Q01.txt",'r')
all_text = FH.read()
all_lines = all_text.strip().split('\n')
numbers = list()
for num in all_lines:
    x = int(num)
    numbers.append(x)

print(numbers)
print("maximum number:",max(numbers))
print("Sum of all the numbers in the list:",sum(numbers))

