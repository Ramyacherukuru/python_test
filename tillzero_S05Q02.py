first_iter = True
count_1 = 0
count_2 = 0
count_3 = 0
while True:
        a = int(input("Enter the value of 'a':"))
        if a == 0:
                break
        if first_iter == True:
                #This is first iteration
                maxv = a
                minv = a
                first_iter = False
        
        
        if a > maxv:
                maxv = a
        if a < minv:
                minv  = a
        
        
        if a < 10:
                count_1 = count_1 + 1
        elif a >= 10 and a < 100:
                
                count_2 = count_2 + 1
        elif a >= 100 and a < 1000:
                count_3 = count_3 + 1
                
                
print("Maximum value :", maxv)
print("Minimum value :",minv)
print("Single digit number:",count_1)            
print("Two digit number:",count_2)
print("Three digit number:",count_3)
