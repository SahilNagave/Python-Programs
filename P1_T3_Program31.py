# BMI calculator.

def calculate_bmi(weight, height):

    if weight > 0 and height > 0:

        bmi = weight / (height**2)
        return bmi

    return None
    
def main():

    weight = float(input("Enter the weight(kg) : "))
    height = float(input("Enter the height(m)  : "))

    result = calculate_bmi(weight, height)

    if result == None:
        print("Enter valid info")

    elif result < 18.5:
        print(f"BMI is {result:.2f} which is Underweight")
    
    elif result <= 24.9:
        print(f"BMI is {result:.2f} which is Normal weight")
    
    elif result <= 29.9:
        print(f"BMI is {result:.2f} which is Overweight")
    
    else:
        print(f"BMI is {result:.2f} which is Obese")

if __name__ == "__main__":
    main()