# Find the sum of even numbers up to N.

def main():

    number = int(input("Enter the number : "))
    result = 0

    for i in range(2, number+1, 2):
        result += i

    print(f"Sum of even numbers up to {number} is : {result}")
    
if __name__ == "__main__":
    main()