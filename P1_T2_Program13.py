# Find the last digit of a number.

def find_last_digit(value):

    no = abs(value)
    return no % 10

def main():

    num = int(input("Enter a number : "))

    lst_digit = find_last_digit(num)
    print(f"The last digit is : {lst_digit}")

if __name__ == "__main__":
    main()