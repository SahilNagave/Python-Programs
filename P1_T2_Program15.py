# Reverse a two-digit number.

def reverse_number(value):

    value   = abs(value)
    reverse = 0

    while (value != 0):
        rem     = value % 10
        reverse = reverse * 10 + rem
        value   = value // 10

    return reverse

def main():

    num = int(input("Enter two-digit number : "))

    ans = reverse_number(num)
    print(f"Reverse number is : {ans}")

if __name__ == "__main__":
    main()