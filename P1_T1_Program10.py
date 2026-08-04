# Find the cube of a number.

def Cube(Value):
    return Value**3

def main():

    Num = int(input("Enter the number : "))
    Ret = Cube(Num)
    print(f"Cube of {Num} is : {Ret}")

if __name__ == "__main__":
    main()