# Reverse a number.

def reverse_number(number):

    temp = abs(number)

    if temp == 0:
        return 0

    reverse = 0

    while temp > 0:
        remainder = temp % 10
        reverse   = reverse * 10 + remainder
        temp      = temp // 10

    return reverse

def main():

    number = int(input("Enter the number : "))

    result = reverse_number(number)
    print(f"The reversed number is : {result}")

if __name__ == "__main__":
    main()