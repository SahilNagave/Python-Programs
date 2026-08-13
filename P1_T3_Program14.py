# Income tax calculator.

def calculate_income_tax(annual_income):

    if (annual_income <= 250000):
        income_tax = 0

    elif (annual_income <= 500000):
        income_tax = (annual_income - 250000 )* 5 / 100

    elif (annual_income <= 1000000):
        income_tax = (250000 * 5 / 100) + ((annual_income - 500000) * 20 / 100)

    else:
        income_tax = (250000 * 5 / 100) + (500000 * 20 / 100) + ((annual_income - 1000000) * 30 / 100)

    return income_tax 

def main():

    annual_income = float(input("Enter the annual income : "))

    income_tax    = calculate_income_tax(annual_income)
    print(f"For ₹{annual_income} of annual income the income tax is : ₹{income_tax}")

if __name__ == "__main__":
    main()