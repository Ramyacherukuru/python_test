def ask_to_continue():
    while True:
        user_input = input("Do you want to continue? (yes/no): ")
        if user_input.lower() == "yes":
            print("continue")
            return True
        elif user_input.lower() == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

while True:

    if not ask_to_continue():
        break
