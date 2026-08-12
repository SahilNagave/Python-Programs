# Grade calculator.

def grade_calculator(marks):

    if (0 <= marks <= 100):

        if (marks >= 90):
            return "A"

        elif (marks >= 75):
            return "B"

        elif (marks >= 65):
            return "C"

        elif (marks >= 55):
            return "D"

        else:
            return "Fail"
    else:
        return "invalid marks"

def main():

    marks = float(input("Enter the marks : "))

    result = grade_calculator(marks)
    print(f"Grade : {result}")

if __name__ == "__main__":
    main()