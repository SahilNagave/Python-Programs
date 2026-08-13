# Find the type of triangle.

def triangle_type(first, second, third):
          
    if ((first + second > third) and (first + third > second) and (second + third > first)):
        
        if (first == second == third):
            return "Equilateral Triangle"

        elif (first == second or first == third or second == third):
            return "Isosceles Triangle"

        else:
            return "Scalene Triangle"
    
    else:
        return "Not a valid triangle"
    
def main():

    first, second, third = map(int, input("Enter 3 sides of triangles : ").split())

    result = triangle_type(first, second, third)
    print(result)

if __name__ == "__main__":
    main()