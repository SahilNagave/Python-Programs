# Find whether a number is divisible by both 5 and 11.

def is_divisible_by_5_and_11(number):

    if (number % 5 == 0 and number % 11 == 0):
        return True

    return False

def main():

    number = int(input("Enter a number : "))

    result = is_divisible_by_5_and_11(number)

    if result:
        print(f"{number} is divisible by both 5 & 11")

    else:
        print(f"{number} is NOT divisible by both 5 & 11")

if __name__ == "__main__":
    main()