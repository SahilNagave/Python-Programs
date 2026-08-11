# Check voting eligibility.

def voting_eligibility(age):

    if (age >= 18):
        return True

    return False

def main():

    age = int(input("Enter the AGE : "))

    ret = voting_eligibility(age)

    if (ret):
        print("You are Eligible to Vote.")

    else:
        print("You are NOT Eligible to Vote.")

if __name__ == "__main__":
    main()