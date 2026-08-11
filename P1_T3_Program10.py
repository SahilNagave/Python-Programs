# Check whether a character is uppercase or lowercase.

def character_check(char):
        
        if (char >= "A" and char <= "Z"):
            return "uppercase"
        
        elif (char >= "a" and char <= "z"):
            return "lowercase"
        
        else:            
            return "Neither uppercase nor lowercase"
    
def main():

    character = input("Enter the character : ")

    result    = character_check(character)
    print(f"The character is : {result}")


if __name__ == "__main__":
    main()