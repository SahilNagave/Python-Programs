# Check whether three angles form a triangle.

def check_triangle(first, second, third):

    if ((first > 0 and second > 0 and third > 0) and (first + second + third == 180)):
        return "Forms a triangle"

    return "Does not forms a triangle"

def main():

    first, second, third = map(float, input("Enter 3 angles : ").split())

    result = check_triangle(first, second, third)
    print(result)

if __name__ == "__main__":
    main()