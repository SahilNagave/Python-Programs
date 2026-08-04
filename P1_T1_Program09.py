# Find the square of a number.

def Square(Value):
    return Value**2

def main():

    Num = int(input("Enter the number : "))
    Ret = Square(Num)
    print(f"Square of {Num} is : {Ret}")

if __name__ == "__main__":
    main()