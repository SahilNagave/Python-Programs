# Find the smallest of three numbers.

def smallest(num1, num2, num3):

    if (num1 < num2 and num1 < num3):
        return num1

    elif (num2 < num3):
        return num2

    else:
        return num3

def main():

    num1, num2, num3 = map(int,input("Enter three numbers : ").split())

    ans = smallest(num1, num2, num3)
    print(f"Smallest number is : {ans}")

if __name__ == "__main__":
    main()