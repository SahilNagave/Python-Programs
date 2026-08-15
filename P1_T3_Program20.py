# Check whether a character is a digit.

def check_character(character):

    if len(character) == 1 and ("0" <= character <= "9"):
        return "DIGIT"

    return "NOT DIGIT"

def main():

    character = input("Enter the character : ")

    result    = check_character(character)
    print(f"The character is : {result}")

if __name__ == "__main__":
    main()