# Calculate GST amount and final bill.

def calculate_bill(original_bill, gst_percentage):

    gst_amount = original_bill * gst_percentage / 100
    final_bill = original_bill + gst_amount

    return (gst_amount, final_bill)

def main():

    original_bill  = float(input("Enter the ORIGINAL BILL :  "))
    gst_percentage = float(input("Enter the GST PERCENTAGE : "))

    gst_amount, final_bill = calculate_bill(original_bill, gst_percentage)
    print(f"The GST amount is --> {gst_amount}\nFinal bill is --> {final_bill}")

if __name__ == "__main__":
    main()