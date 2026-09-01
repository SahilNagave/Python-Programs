# Check whether a number is a palindrome.

def check_palindrome(number):

    original = abs(number)
    temp     = original

    reverse = 0

    while temp > 0:
        remainder = temp % 10
        reverse   = reverse * 10 + remainder
        temp      = temp // 10

    if original == reverse:
        return True

    return False

def main():

    number = int(input("Enter the number : "))

    result = check_palindrome(number)
    if result:
        print(f"{number} is PALINDROME")

    else:
        print(f"{number} is NOT PALINDROME")
    
if __name__ == "__main__":
    main()