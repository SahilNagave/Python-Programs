# Calculate the power of a number

def calculate_power(number, exponent):
    return (number ** exponent)

def main():

    base  = int(input("Enter the base : "))
    power = int(input("Enter the power : "))

    ans   = calculate_power(base, power)
    print(f"The power of {base} raised to {power} is: {ans}")

if __name__ == "__main__":
    main()