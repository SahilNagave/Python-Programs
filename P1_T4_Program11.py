# Find factorial of a number.

def factorial_number(number):

    if number < 0:
        return None

    factorial = 1

    for i in range(1, number+1):
        factorial *= i

    return factorial

def main():

    number = int(input("Enter the number : "))

    result = factorial_number(number)

    if result is not None:
        print(f"The factorial of {number} is : {result}")

    else:
        print("Invalid Factorial Input")

if __name__ == "__main__":
    main()