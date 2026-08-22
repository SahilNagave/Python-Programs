# Check whether a student passes based on marks in five subjects.

def check_pass_fail(sub1, sub2, sub3, sub4, sub5):

    minimum_passing_marks = 40

    if (0 <= sub1 <= 100) and (0 <= sub2 <= 100) and (0 <= sub3 <= 100) and (0 <= sub4 <= 100) and (0 <= sub5 <= 100):
        if (sub1 >= minimum_passing_marks) and (sub2 >= minimum_passing_marks) and (sub3 >= minimum_passing_marks) and (sub4 >= minimum_passing_marks) and (sub5 >= minimum_passing_marks):
            return "PASS"

        return "FAIL"

    return "Invalid Marks"

def main():

    sub1, sub2, sub3, sub4, sub5 = map(float, input("Enter the marks for five subjects : ").split())

    result = check_pass_fail(sub1, sub2, sub3, sub4, sub5)
    print(result)

if __name__ == "__main__":
    main()