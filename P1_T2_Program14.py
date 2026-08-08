# Find the first digit of a number.

def find_first_digit(value):

    number = abs(value)

    if (number == 0):
        return 0

    while (number != 0):
        rem    = number % 10
        number = number // 10

    return rem

def main():

    num = int(input("Enter a number : "))

    first_digit = find_first_digit(num)
    print(f"First Digit of {num} is : {first_digit}")

if __name__ == "__main__":
    main()