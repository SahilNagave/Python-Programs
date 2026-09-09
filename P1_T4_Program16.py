# Check whether a number is a Perfect number.

def check_perfect_number(number):

    if number <= 0:
        return False
    
    divisors = 0
    for i in range(1, number):
        if number % i == 0:
            divisors  += i

    if number == divisors:
        return True

    return False

def main():

    number = int(input("Enter the number : "))

    result = check_perfect_number(number)

    if result:
        print(f"{number} is a PERFECT NUMBER")

    else:
        print(f"{number} IS NOT a PERFECT NUMBER")

if __name__ == "__main__":
    main()