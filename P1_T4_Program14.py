# Check whether a number is a Strong number.

def check_strong_number(number):

    if number <= 0:
        return False
    
    original  = number
    total     = 0
    factorial = 1

    while number > 0:
        remainder = number % 10

        for i in range(1, remainder+1):
            factorial = i * factorial
            
        total      = factorial + total
        factorial  = 1

        number = number // 10

    if original == total:
        return True

    return False

def main():

    number = int(input("Enter the number : "))

    result = check_strong_number(number)

    if result:
        print(f"{number} is a STRONG NUMBER")

    else:
        print(f"{number} IS NOT a STRONG NUMBER")

if __name__ == "__main__":
    main()