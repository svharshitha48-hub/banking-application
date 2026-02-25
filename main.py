from services import register_user, login, transfer_fund
from menu import show_menu

def main():
    print("1. Register")
    print("2. Login")

    choice = int(input("Enter choice: "))

    if choice == 1:
        username = input("Username: ")
        address = input("Address: ")
        aadhar = input("Aadhar: ")
        mobile = input("Mobile: ")
        register_user(username, address, aadhar, mobile)

    elif choice == 2:
        username = input("Username: ")
        user = login(username)

        if user:
            while True:
                show_menu()
                option = int(input("Select option: "))

                if option == 3:
                    amount = float(input("Enter amount: "))
                    transfer_fund(user[0], amount)

                elif option == 6:
                    break
        else:
            print("User not found")

if __name__ == "__main__":
    main()