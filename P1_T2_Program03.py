# Find the largest of two numbers.

def largest(value1, value2):

    if value1 > value2:
        return True

    return False

def main():

    no1 = int(input("Enter 1st number : "))
    no2 = int(input("Enter 2nd number : "))

    ans = largest(no1, no2)

    if no1 == no2:
        print(f"{no1} & {no2} are equal to each other")

    elif ans == True:
        print(f"{no1} is largest than {no2}")

    else:
        print(f"{no2} is largest than {no1}")

if __name__ == "__main__":
    main()