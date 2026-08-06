# Check whether a number is even or odd.

def check_even_odd(value):

    if value % 2 == 0:
        return True

    return False
    
def main():

    num = int(input("Enter the number : "))

    ans = check_even_odd(num)

    if ans == True:
        print(f"{num} is EVEN")

    else:
        print(f"{num} is ODD")

if __name__ == "__main__":
    main()