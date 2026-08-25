# Print the multiplication table of a number.

def main():

    number = int(input("Enter the number : "))

    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

if __name__ == "__main__":
    main()