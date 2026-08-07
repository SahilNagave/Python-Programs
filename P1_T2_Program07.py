# Check if two numbers are equal.

def check_equal(num1, num2):

    if num1 == num2:
        return True

    return False

def main():

    no1 = int(input("Enter 1st number : "))
    no2 = int(input("Emter 2nd number : "))

    ans = check_equal(no1, no2)

    if ans == True:
        print(f"{no1} & {no2} are EQUAL to each other")

    else:
        print(f"{no1} & {no2} are NOT EQUAL to each other")

if __name__ == "__main__":
    main()