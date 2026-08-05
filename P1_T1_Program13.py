# Calculate Area and Circumference of a Circle.

def calculate(radius):

    area = 3.14 * radius**2
    circumference = 2 * 3.14 * radius

    return(area, circumference)

def main():

    Radius = float(input("Enter the radius : "))

    area, circumference = calculate(Radius)
    print(f"Area of circle is : {area}\nCircumference of circle is : {circumference}")

if __name__ == "__main__":
    main()