# Check whether a number is a multiple of 10.

def check_multiple(number):

    if (number % 10 == 0):
        return True

    return False

def main():

    number = int(input("Enter the number : "))

    result = check_multiple(number)
    if result:
        print(f"{number} is multiple of 10")

    else:
        print(f"{number} is NOT multiple of 10")

if __name__ == "__main__":
    main()