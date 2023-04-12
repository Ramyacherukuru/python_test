n = int(input("Enter the number1:"))
if n < 10:
    n = n + 7
    print(n%10)
elif n >= 10 and n <= 99:
        n = n ** 5
        print(n%10)
elif n >= 100 and n <= 999:
        n1 = int(input("Enter the another number:"))
        n = n + n1
        print(n%10)
        
        

