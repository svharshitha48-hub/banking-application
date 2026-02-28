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

# Import menu display function
from menu import show_menu


def main():

    print("🏦 Welcome to Harshitha Bank")
    print("1️⃣  Register")
    print("2️⃣  Login")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("❌ Invalid input.")
        return

    # ----------------------------
    # REGISTRATION
    # ----------------------------
    if choice == 1:
        username = input("Username: ")
        address = input("Address: ")
        aadhar = input("Aadhar: ")
        mobile = input("Mobile: ")

        # Ask user to set MPIN
        while True:
            mpin = input("🔐 Set your 4-digit MPIN: ")
            if len(mpin) == 4 and mpin.isdigit():
                break
            else:
                print("❌ MPIN must be exactly 4 digits.")

        register_user(username, address, aadhar, mobile, mpin)

    # ----------------------------
    # LOGIN
    # ----------------------------
    elif choice == 2:
        username = input("Username: ")
        user = login(username)

        if user:
            print(f"\n✅ Welcome {username}!")

            # Keep showing menu until logout
            while True:
                show_menu()

                try:
                    option = int(input("Select option: "))
                except ValueError:
                    print("❌ Invalid input.")
                    continue

                # OPTION 1 → View Account
                if option == 1:
                    view_account_info(user[0])

                

                # OPTION 3 → Transfer Fund
                elif option == 2:
                    try:
                        amount = float(input("Enter amount: "))
                        transfer_fund(user[0], amount)
                    except ValueError:
                        print("❌ Invalid amount.")

                # OPTION 4 → Change MPIN
                elif option == 3:
                    change_mpin(user[0])

                # OPTION 5 → Register New Credit Card
                elif option == 4:
                    register_new_credit_card(user[0])

                # OPTION 6 → View Transactions
                elif option == 5:
                    view_transactions(user[0])

                # OPTION 7 → Logout
                elif option == 6:
                    print("👋 Logged out successfully.")
                    break

                else:
                    print("❌ Invalid option selected.")

        else:
            print("❌ User not found.")

    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()