# Check whether a year is a leap year.

def check_leap_year(year):

    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True

    return False

def main():

    year = int(input("Enter the YEAR : "))

    ret  = check_leap_year(year)

    if (ret):
        print(f"{year} is a LEAP YEAR")

    else:
        print(f"{year} is NOT a LEAP YEAR")


if __name__ == "__main__":
    main()