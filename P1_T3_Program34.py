# Calculate net salary after deductions.

def calculate_net_salary(gross_salary, deduction_percent):

    if gross_salary > 0 and 0 <= deduction_percent <= 100:
        return gross_salary - (gross_salary * deduction_percent / 100)
       
    return None

def main():

    gross_salary      = float(input("Enter the gross salary : ₹"))
    deduction_percent = float(input("Enter the deduction percentage : "))

    result = calculate_net_salary(gross_salary, deduction_percent)

    if result is not None:
        print(f"Your Net salary is : ₹{result:.2f}")

    else:
        print("Invalid Inputs")

if __name__ == "__main__":
    main()