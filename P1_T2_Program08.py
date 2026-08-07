# Check whether a number is positive, negative, or zero.

def check_number(no):

    if no > 0 :
        return 1  ## 1 --> POSITIVE NUMBER

    elif no < 0 :
        return -1 ## -1 --> NEGATIVE NUMBER
        
    else:
        return 0  ## 0 --> ZERO NUMBER
        
def main():

    num = int(input("Enter the number : "))
    ans = check_number(num)

    if ans == 1 :
        print(f"{num} is a POSITIVE number")

    elif ans == -1 :
        print(f"{num} is a NEGATIVE number")

    else:
        print(f"{num} is a ZERO number")

if __name__ == "__main__":
    main()