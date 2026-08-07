# Convert minutes into hours and minutes.

def convert_minutes(total_minutes):

    hours   = total_minutes // 60
    minutes = total_minutes % 60

    return (hours, minutes)

def main():

    minutes = int(input("Enter the number of minutes : "))

    hrs, mts = convert_minutes(minutes)
    print(f"{minutes} minutes means {hrs} hours & {mts} minutes")

if __name__ == "__main__":
    main()