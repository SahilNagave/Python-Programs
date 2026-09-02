# Check whether a number is an Armstrong number.

def check_armstrong(number):

    original = number
    temp     = original

    count = 0
    while temp > 0:
        count += 1
        temp //= 10

    total = 0
    while number > 0:
        remainder = number % 10
        total     = total + remainder ** count
        number    = number // 10

    if original == total:
        return True

    return False

def main():

    number = int(input("Enter the number : "))

    result = check_armstrong(number)
    if result:
        print(f"{number} is a ARMSTRONG number")

    else:
        print(f"{number} IS NOT a ARMSTRONG number")

if __name__ == "__main__":
    main() 