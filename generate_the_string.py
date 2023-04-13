n = int(input("Enter the number:"))
gen= ""
for i in range(0, n):
    i = str(i)
    x = i * (n - 1)
    gen = gen + x
    
print(gen)
