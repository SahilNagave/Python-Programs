# Find the sum of the first N natural numbers.

def main():

    number = int(input("Enter the number : "))
    result = 0

    for i in range(1, number+1):
        result += i

    print(f"Sum of the first N natural numbers is : {result}")
    
if __name__ == "__main__":
    main()