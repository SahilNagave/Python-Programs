# Movie ticket price calculator.

def calculate_ticket_price(age, tickets):

    if (age > 0 and tickets > 0):
        
        if (age < 5):
            return "Total Price : ₹0"

        elif (age <= 17):
            return f"Total Price : ₹{tickets * 100}"

        elif (age <= 59):
            return f"Total Price : ₹{tickets * 200}"

        else:
            return f"Total Price : ₹{tickets * 150}"
        
    return "Invalid Age or Tickets"

def main():

    age = int(input("Enter the age : "))
    tickets = int(input("Enter the number of tickets : "))

    price = calculate_ticket_price(age, tickets)
    print(price)

if __name__ == "__main__":
    main()