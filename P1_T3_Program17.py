# Check whether a triangle is valid.

def triangle_validity(first, second, third):
          
    if ((first + second > third) and (first + third > second) and (second + third > first)):
        return "Valid Triangle"
    
    else:
        return "Not a valid triangle"
    
def main():

    first, second, third = map(int, input("Enter 3 sides of triangles : ").split())

    result = triangle_validity(first, second, third)
    print(result)

if __name__ == "__main__":
    main()