# Import required functions from services.py
from services import (
    register_user,
    login,
    transfer_fund,
    view_account_info,
    change_mpin,
    register_new_credit_card,
    view_transactions
)
# Import validation functions
from validation import (
    validate_username,
    validate_aadhar,
    validate_mobile,
    validate_pin,
    validate_amount
)

# Import menu display function
from menu import show_menu


def main():

    print("🏦 Welcome to Harshitha Bank")
    print("1️⃣  Register")
    print("2️⃣  Login")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input.")
        return

    # ============================
    # REGISTRATION
    # ============================
    if choice == 1:

        # Username validation
        while True:
            username = input("Username: ")
            if validate_username(username):
                break

        address = input("Address: ")

        # Aadhar validation
        while True:
            aadhar = input("Aadhar: ")
            if validate_aadhar(aadhar):
                break

        # Mobile validation
        while True:
            mobile = input("Mobile: ")
            if validate_mobile(mobile):
                break
                
        # MPIN validation
        while True:
            mpin = input("Set your 4-digit MPIN: ")
            if validate_pin(mpin):
                break

        register_user(username, address, aadhar, mobile, mpin)

    # ============================
    # LOGIN
    # ============================
    elif choice == 2:

        username = input("Username: ")
        user = login(username)

        if user:
            print(f"\nWelcome {username}!")

            while True:
                show_menu()

                try:
                    option = int(input("Select option: "))
                except ValueError:
                    print("Invalid input.")
                    continue

                # 1️⃣ View Account
                if option == 1:
                    view_account_info(user[0])

                # 2️⃣ Transfer Fund
                elif option == 2:
                    try:
                        amount = float(input("Enter amount: "))
                        if not validate_amount(amount):
                            continue
                        transfer_fund(user[0], amount)
                    except ValueError:
                        print("Invalid amount.")

                # 3️⃣ Change MPIN
                elif option == 3:
                    change_mpin(user[0])

                # 4️⃣ Register Credit Card
                elif option == 4:
                    register_new_credit_card(user[0])

                # 5️⃣ View Transactions
                elif option == 5:
                    view_transactions(user[0])

                # 6️⃣ Logout
                elif option == 6:
                    print(" Logged out successfully.")
                    break

                else:
                    print("Invalid option selected.")

        else:
            print("User not found.")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()