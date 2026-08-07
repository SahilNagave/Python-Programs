# Convert days into years, months, and days (assume 30-day months, 365-day years).

def convert_days(total_days):

    years          = total_days // 365
    remaining_days =  total_days % 365
    months         = remaining_days // 30
    days           = remaining_days % 30

    return (years, months, days)

def main():

    days = int(input("Enter the number of days : "))

    yrs, mnts, dys = convert_days(days)
    print(f"{days} days means {yrs} years, {mnts} months & {dys} days")

if __name__ == "__main__":
    main()