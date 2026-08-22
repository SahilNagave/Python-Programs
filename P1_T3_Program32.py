# Calculate profit or loss.

def calculate_profit_loss(cost_price, selling_price):

    if cost_price > 0 and selling_price > 0:

        if selling_price > cost_price:
            return f"PROFIT --> ₹{selling_price - cost_price}"

        elif cost_price > selling_price:
            return f"LOSS --> ₹{cost_price - selling_price}"

        else:
            return "No Profit, No Loss"

    return "Invalid Inputs"
        
def main():

    cost_price    = float(input("Enter the cost price : ₹"))
    selling_price = float(input("Enter the selling price : ₹"))

    result = calculate_profit_loss(cost_price, selling_price)
    print(result)

if __name__ == "__main__":
    main()