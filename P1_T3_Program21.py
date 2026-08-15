# Check whether a character is a special character.

def check_character(character):

    if len(character) == 1:
        if (("a" <= character <= "z") or ("A" <= character <= "Z") or ("0" <= character <= "9")):
            return "NOT A SPECIAL CHARACTER"

        return "SPECIAL CHARACTER"

    return "NOT A CHARACTER"

def main():

    character = input("Enter the character : ")

    result    = check_character(character)
    print(f"The character is : {result}")

if __name__ == "__main__":
    main()