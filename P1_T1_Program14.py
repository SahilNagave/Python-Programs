# Convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(C):
    return (C * 9/5) + 32 

def main():

    celsius = float(input("Enter temperature in Celsius : "))
    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"Temperature after conversion is : {fahrenheit}")

if __name__ == "__main__":
    main()