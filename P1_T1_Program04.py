# Input two numbers and print their difference.

def Difference(Value1 , Value2):
    return Value1 - Value2

def main():

    NO1 = int(input("Enter 1st number : "))
    NO2 = int(input("Enter 2nd number : "))

    Ret = Difference(NO1 , NO2)
    print(f"Difference of {NO1} & {NO2} is : {Ret}")

if __name__ == "__main__":
    main()