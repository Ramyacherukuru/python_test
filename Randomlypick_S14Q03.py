import random
numbers = []
for num in range(10):
    number = int(input(f"Enter the number {num+1}:"))
    numbers.append(number)
random_numbers = random.sample(numbers,5)
print("Random numbers:", random_numbers)
print("original numbers:",numbers)


