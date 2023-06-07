prime = []
FH = open("num.txt", 'r')
all_text = FH.read()
all_lines = all_text.strip().split('\n')
print(all_lines)


for line in all_lines:
    num = int(line)   

    if not(num > 99 and num < 1000):
        continue
    
     
    for i in range(2, num // 2 + 1):
        if(num % i) == 0:
            break   
    else:
        prime.append(num)
        
prime = sorted(prime  , reverse = True)
print("Sorted prime number:", prime)




