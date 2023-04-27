def get_number():
    
    number = int(input("Enter a number:"))
    number = int(number) 
    return number


def print_mtable(number):
    for i in range(1, 11):
        print(number,"*",i,"=",number*i)
                   
    

def main():
    
    inp = get_number()
    print_mtable(inp)

# Main starts from here
main()
