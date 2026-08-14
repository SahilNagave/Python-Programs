# Check whether a character is an alphabet.

def check_character(character):

    if (("a" <= character <= "z") or ("A" <= character <= "Z")):
        return "ALPHABET"

    return "NOT ALPHABET"

def main():

    character = input("Enter the character : ")

    result    = check_character(character)
    print(f"The character is {result}")

if __name__ == "__main__":
    main()