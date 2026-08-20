# Mobile recharge offer calculator.

def offer_calculator(recharge_amount):

    if recharge_amount > 0:

        if recharge_amount < 100:
            return("No Offer")

        elif recharge_amount < 300:
            return(f"5% cashback\ncashback amount : ₹{recharge_amount * 0.05}")

        elif recharge_amount < 500:
            return(f"10% cashback\ncashback amount : ₹{recharge_amount * 0.1}")
            
        else:
            return(f"20% cashback\ncashback amount : ₹{recharge_amount * 0.2}")
            
    return("Invalid Recharge Amount")
    
def main():

    recharge_amount = float(input("Enter the recharge amount : ₹"))

    result = offer_calculator(recharge_amount)
    print(result)

if __name__ == "__main__":
    main()