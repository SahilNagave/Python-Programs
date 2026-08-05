# Calculate Compound Interest.

def compound_interest(principal_amount, rate, time):

    decimal_rate = rate / 100

    final_amount = principal_amount * (1 + decimal_rate)**time

    return (final_amount - principal_amount)

def main():

    Principal = float(input("Enter the principal amount : "))
    Rate      = float(input("Enter the rate of interest : "))
    Time      = float(input("Enter the time : "))

    C_I = compound_interest(Principal, Rate, Time)
    print(f"The Compound Interest is : {C_I}")

if __name__ == "__main__":
    main()