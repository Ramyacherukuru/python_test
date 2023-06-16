filename = input("Enter the file name: ")

names = []
with open(filename, 'r') as FH:
    for line in FH:
        name,_  = line.strip().split(':')
        names.append(name)

user = input("Enter a few characters to search for: ")

matching_names = []
for name in names:
    if user in name:
        matching_names.append(name)

matching_names.sort()

for name in matching_names:
    print(name)
  
