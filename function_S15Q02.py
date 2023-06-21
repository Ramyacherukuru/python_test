list1 = [4,17,21,47,69,75,91,97]
list2 = [3,10,11,14,18,21,44,55,76,97]

new_list = []
list1_index = 0
list2_index = 0

while list1_index < len(list1) and list2_index < len(list2):

    if list1[list1_index] <= list2[list2_index]:
        new_list.append(list1[list1_index])
        list1_index += 1

    else:
         new_list.append(list2[list2_index])
         list2_index += 1

while list1_index < len(list1):
    new_list.append(list1[list1_index])
    list1_index += 1
    

while list2_index < len(list2):
    new_list.append(list2[list2_index])
    list2_index += 1

print("Sorted Result:", new_list)
