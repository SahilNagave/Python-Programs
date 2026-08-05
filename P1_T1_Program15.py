# Calculate the average of five numbers.

def average(A, B, C, D, E):
    return (A + B + C + D + E ) / 5

def main():

    a = float(input("Enter the 1st number : "))
    b = float(input("Enter the 2nd number : "))
    c = float(input("Enter the 3rd number : "))
    d = float(input("Enter the 4th number : "))
    e = float(input("Enter the 5th number : "))

    ret = average(a, b, c, d, e)

    print(f"Average of the entered numbers is : {ret}")

if __name__ == "__main__":
    main()