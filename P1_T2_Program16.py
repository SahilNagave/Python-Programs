# Reverse a three-digit number (without loops).

def reverse_number(value):

    number = abs(value)

    last_digit         = number % 10
    removed_last_digit = number // 10
    middle_digit       = removed_last_digit % 10
    first_digit        = removed_last_digit // 10

    return (last_digit, middle_digit, first_digit)

def main():

    num = int(input("Enter a three-digit number : "))

    last, middle, first = reverse_number(num)
    print(f"Reversed number is : {last}{middle}{first}")

if __name__ == "__main__":
    main()