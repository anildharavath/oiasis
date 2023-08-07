import hashlib

def get_user_credentials():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username, password = get_user_credentials()
    hashed_password = hash_password(password)
    with open('users.txt', 'a') as file:
        file.write(f"{username}:{hashed_password}\n")
    print("Registration successful!")

def login():
    username, password = get_user_credentials()
    hashed_password = hash_password(password)
    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, stored_hashed_password = line.strip().split(':')
            if stored_username == username and stored_hashed_password == hashed_password:
                print("Login successful!")
                return True
        print("Invalid username or password.")
        return False

def secured_page():
    print("Welcome to the secured page!")
    # Add your secured page logic here

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                secured_page()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
