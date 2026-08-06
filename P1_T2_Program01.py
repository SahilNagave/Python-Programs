# Find remainder without using %.

def remainder(value1, value2):

    quotient = value1 // value2
    return (value1 - quotient * value2)

def main():

    no1 = int(input("Enter 1st number : "))
    no2 = int(input("Enter 2nd number : "))

    ans = remainder(no1, no2)
    print(f"The remainder of {no1} & {no2} is : {ans}")

if __name__ == "__main__":
    main()