# Login system using username and password.

def login_system(username, password):

    correct_username = "admin"
    correct_password = "Admin@123"

    if username == correct_username and password == correct_password:
        return True

    return False

def main():

    username = input("Enter the username : ")
    password = input("Enter the password : ")

    result   = login_system(username, password)
    if result:
        print("LOGIN SUCCESSFULLY")

    else:
        print("LOGIN FAILED")

if __name__ == "__main__":
    main()