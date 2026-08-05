# Calculate Simple Interest.

def Simple_Interest(principal_amount, rate, time):
    return (principal_amount * rate * time ) // 100

def main():

    Principal = float(input("Enter the principal amount : "))
    Rate      = float(input("Enter the rate of interest : "))
    Time      = float(input("Enter the time : "))

    S_I = Simple_Interest(Principal, Rate, Time)
    print(f"The Simple Interest is : {S_I}")

if __name__ == "__main__":
    main()