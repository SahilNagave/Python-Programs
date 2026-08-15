# Find the largest among four numbers.

def check_largest(first, second, third, fourth):

    if ((first > second) and (first > third) and (first > fourth)):
        return first

    elif ((second > third) and (second > fourth)):
        return second

    elif (third > fourth):
        return third

    else:
        return fourth
    
def main():

    first, second, third, fourth = map(float, input("Enter 4 numbers : ").split())

    result = check_largest(first, second, third, fourth)
    print(f"The largest among four numbers is : {result}")

if __name__ == "__main__":
    main()