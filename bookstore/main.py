from admin import Admin

def main():
    while True:
        print("""
            1. Login
            2. Exit
            """)
        ch = input("Enter choice: ")

        if ch == '1':
            uname = input("Enter Username: ")
            passw = input("Enter Password: ")

            if uname == "admin" and passw == "1234":
                print("Login Successful")
                Admin()   
            else:
                print("Invalid credential")
            
        elif ch == '2':
            print("Thank you!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
