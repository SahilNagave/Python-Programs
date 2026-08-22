# Restaurant bill with GST and discount.

def calculate_bill(original_bill):

    if original_bill > 0:
        if original_bill >= 1000:
            discount_amount = original_bill * 0.1

        else:
            discount_amount = 0

        gst_amount = original_bill * 0.05
        final_bill = original_bill - discount_amount + gst_amount
        
        return (discount_amount, gst_amount, final_bill)

    return None, None, None

def main():

    original_bill = float(input("Enter the original bill : ₹"))

    discount_amount, gst_amount, final_bill = calculate_bill(original_bill)

    if final_bill is not None:
        print(f"\nOriginal Bill : ₹{original_bill:.2f}\nDiscount amount: ₹{discount_amount:.2f}\nGST(5%) : ₹{gst_amount:.2f}\n\nFinal Bill : ₹{final_bill:.2f}")

    else:
        print("Enter Valid Bill")

if __name__ == "__main__":
    main()