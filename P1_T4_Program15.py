# Check whether a number is a Neon number.

def check_neon_number(number):

    total   = 0
    square  = number ** 2

    while square > 0:
        remainder = square % 10
        total     =  total + remainder
        square    = square // 10

    if number == total:
        return True

    return False

def main():

    number = int(input("Enter the number : "))

    result = check_neon_number(number)

    if result:
        print(f"{number} is a NEON NUMBER")

    else:
        print(f"{number} IS NOT a NEON NUMBER")

if __name__ == "__main__":
    main()