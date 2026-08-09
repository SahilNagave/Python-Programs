# Calculate the total salary using basic salary, HRA, and DA.

def calculate_salary(basic_salary, hra, da):

    total_salary =  basic_salary + hra + da
    return (total_salary)

def main():

    basic_salary = float(input("Enter the BASIC SALARY : "))
    hra          = float(input("Enter the HRA : "))
    da           = float(input("Enter the DA : "))

    cmplt_slry = calculate_salary(basic_salary, hra, da)
    print(f"The total salary is : {cmplt_slry}")

if __name__ == "__main__":
    main()