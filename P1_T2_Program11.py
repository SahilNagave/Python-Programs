# Convert kilometers to meters and centimeters.

def convert_distance(km):

    meters      = km * 1000
    centimeters = meters * 100

    return(meters, centimeters)

def main():

    kilometers = float(input("Enter the kilometers : "))

    mts, cm    = convert_distance(kilometers)
    print(f"{kilometers} kilometers means {mts} meters & {cm} centimeters")

if __name__ == "__main__":
    main()