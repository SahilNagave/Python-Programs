# Electricity bill calculator.

def calculate_electricity_bill(units_consumed):

    fixed_rate_per_unit = 8
    electricity_bill    = units_consumed * fixed_rate_per_unit
    return (electricity_bill)

def main():

    units_consumed = float(input("Enter the units consumed : "))

    total_bill = calculate_electricity_bill(units_consumed)
    print(f"The electricity bill is : {total_bill}")

if __name__ == "__main__":
    main()