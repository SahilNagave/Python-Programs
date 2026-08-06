# Find the absolute difference between two numbers.

def absolute_difference(value1, value2):

    if value1 > value2:
        return value1 - value2
    
    return value2 - value1

def main():

    no1 = int(input("Enter 1st number : "))
    no2 = int(input("Enter 2nd number : "))

    abs_diff = absolute_difference(no1, no2)

    print(f"The absolute difference between {no1} & {no2} is : {abs_diff}") 

if __name__ == "__main__":
    main()