# Check driving eligibility.

def driving_eligibility(age):

    if (age >= 18):
        return True

    return False

def main():

    age = int(input("Enter the AGE : "))

    ret = driving_eligibility(age)

    if (ret):
        print("You are Eligible to Drive.")

    else:
        print("You are NOT Eligible to Drive.")

if __name__ == "__main__":
    main()