# ATM withdrawal simulation.

def ATM_simulation(current_balance, withdraw_amount):

    if ((withdraw_amount > 0) and (withdraw_amount <= current_balance)):
            current_balance -= withdraw_amount
            return (f"Remaining Balance : ₹{current_balance}")
    
    elif (withdraw_amount > current_balance):
         return "Insufficient balance"

    elif (withdraw_amount <= 0):
        return "Invalid withdrawal amount"

def main():

    current_balance = float(input("Enter the Current balance   : ₹ "))
    withdraw_amount = float(input("Enter the Withdrawal amount : ₹ "))

    result = ATM_simulation(current_balance, withdraw_amount)
    print(result)

if __name__ == "__main__":
    main()