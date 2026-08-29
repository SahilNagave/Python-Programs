# Count digits in a number.

def count_digits(number):

    temp = abs(number)

    if temp == 0:
        return 1

    count = 0

    while temp > 0:
        count += 1
        temp //= 10

    return count

def main():

    number = int(input("Enter the number : "))

    result = count_digits(number)
    print(f"Total number of digits are : {result}")

if __name__ == "__main__":
    main()