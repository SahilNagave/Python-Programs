# Swap two numbers without using a third variable.

def Swap(Value1 , Value2):

    Value1 , Value2 = Value2 , Value1
    return Value1 , Value2

def main():

    NO1 = int(input("Enter 1st number : "))
    NO2 = int(input("Enter 2nd number : "))
    print(f"Numbers Before Swapping : Num1 = {NO1} & Num2 = {NO2}")
    
    NO1 , NO2 = Swap(NO1 , NO2)
    print(f"Numbers After Swapping  : Num1 = {NO1} & Num2 = {NO2}")

if __name__ == "__main__":
    main()