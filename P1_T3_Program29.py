# Railway fare calculator.

def calculate_railway_fare(age, distance):

    base_fare = 2

    if (distance > 0 and age > 0):

        normal_fare = distance * base_fare

        if (age < 5):
            final_fare = 0

        elif (age <= 17):
            final_fare = normal_fare * 0.5

        elif (age <= 59):
            final_fare = normal_fare

        else:
            final_fare = normal_fare * 0.7

        return final_fare

    return "Invalid Distance or Age"
    
def main():

    age      = float(input("Enter the age : "))
    distance = float(input("Enter the distance in km : "))

    final_fare = calculate_railway_fare(age, distance)
    print(f"The final fare is : ₹{final_fare}")

if __name__ == "__main__":
    main()