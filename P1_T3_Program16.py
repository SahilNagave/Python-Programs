# Calculate bonus based on years of service.

def calculate_bonus(service, salary):

    if (service < 5):
        bonus = 0

    elif (5 <= service <= 10):
        bonus = salary * 10 / 100

    else:
        bonus = salary * 20 / 100

    return bonus

def main():

    service = float(input("Enter the years of service : "))
    salary  = float(input("Enter the salary : "))

    bonus   = calculate_bonus(service, salary)
    print(f"You have got ₹{bonus} BONUS")

if __name__ == "__main__":
    main()