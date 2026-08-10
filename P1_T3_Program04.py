# Find the largest of three numbers.

def largest(num1, num2, num3):

    if (num1 > num2 and num1 > num3):
        return num1

    elif (num2 > num3):
        return num2

    else:
        return num3

def main():

    num1, num2, num3 = map(int,input("Enter three numbers : ").split())

    ans = largest(num1, num2, num3)
    print(f"Largest number is : {ans}")

if __name__ == "__main__":
    main()