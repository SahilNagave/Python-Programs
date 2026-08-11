# Check whether a character is a vowel or consonant.

def check_character(character):

    if character.isalpha():
        if character in "aeiouAEIOU":
            return "vowel"

        return "consonant"

    return "invalid character"
    
def main():

    character = input("Enter the character : ")

    result    = check_character(character)
    print(f"{character} is a {result}")

if __name__ == "__main__":
    main()