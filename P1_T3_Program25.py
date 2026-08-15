# Check whether a person gets a discount based on age.

def calculate_discount(age):

    if (age > 0):
           
        if (age < 5):
            return "Discount : 20 %"

        elif (5 <= age <= 17):
            return "Discount : 10 %"

        elif (18 <= age <= 59):
            return "Discount : 0 %"

        else:
            return "Discount : 25 %"
            
    return "Invalid Age"

def main():

    age = int(input("Enter the age : "))

    result = calculate_discount(age)
    print(result)

if __name__ == "__main__":
    main()