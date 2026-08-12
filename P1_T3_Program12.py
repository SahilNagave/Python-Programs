# Find whether a number is divisible by 3 or 7.

def is_divisible_by_3_or_7(number):

    if (number % 3 == 0 or number % 7 == 0):
        return True

    return False
    
def main():

    number = int(input("Enter a number : "))

    result = is_divisible_by_3_or_7(number)

    if result:
        print(f"{number} is divisible by 3 or 7")

    else:
        print(f"{number} is NOT divisible by 3 or 7")

if __name__ == "__main__":
    main()