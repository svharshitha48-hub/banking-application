# Import database connection function
from db import get_connection
import random


# -----------------------------------------
# USER REGISTRATION FUNCTION
# -----------------------------------------
def register_user(username, address, aadhar, mobile, mpin):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)

    try:
        # Insert user
        cursor.execute("""
            INSERT INTO users (username, address, aadhar, mobile)
            VALUES (%s, %s, %s, %s)
        """, (username, address, aadhar, mobile))

        user_id = cursor.lastrowid

        # Generate account number
        account_number = "AC" + str(random.randint(10000000, 99999999))

        # Insert account
        cursor.execute("""
            INSERT INTO accounts (user_id, account_number, account_type, balance)
            VALUES (%s, %s, %s, %s)
        """, (user_id, account_number, "Savings", 10000))

        # Create Debit Card
        cursor.execute("""
            INSERT INTO cards (user_id, card_type, pin, cvv)
            VALUES (%s, %s, %s, %s)
        """, (user_id, "Debit", mpin, str(random.randint(100, 999))))

        # Create Credit Card
        cursor.execute("""
            INSERT INTO cards (user_id, card_type, pin, cvv)
            VALUES (%s, %s, %s, %s)
        """, (user_id, "Credit", "5678", str(random.randint(100, 999))))

        conn.commit()

        print("✅ Registration successful.")
        print("🏦 Your Account Number is:", account_number)
        print("Please login.")

    except Exception as e:
        conn.rollback()
        print("❌ Error during registration:", e)

    finally:
        cursor.close()
        conn.close()


# -----------------------------------------
# LOGIN FUNCTION
# -----------------------------------------
def login(username):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)

    try:
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        return cursor.fetchone()

    except Exception as e:
        print("Login error:", e)
        return None

    finally:
        cursor.close()
        conn.close()


# -----------------------------------------
# TRANSFER FUND FUNCTION
# -----------------------------------------
def transfer_fund(user_id, amount):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)

    try:
        # Step 1: Verify MPIN
        entered_pin = input("🔐 Enter your Debit Card MPIN: ")

        cursor.execute("""
            SELECT pin FROM cards
            WHERE user_id=%s AND card_type='Debit'
        """, (user_id,))
        card = cursor.fetchone()

        if not card:
            print("❌ Debit card not found.")
            return

        stored_pin = card[0]

        if entered_pin != stored_pin:
            print("❌ Incorrect MPIN. Transaction cancelled.")
            return

        # Step 2: Ask receiver username
        receiver_username = input("👤 Enter receiver username: ")

        cursor.execute("""
            SELECT id FROM users WHERE username=%s
        """, (receiver_username,))
        receiver = cursor.fetchone()

        if not receiver:
            print("❌ Receiver not found.")
            return

        receiver_id = receiver[0]

        if receiver_id == user_id:
            print("❌ Cannot transfer to yourself.")
            return

        # Step 3: Check sender balance
        cursor.execute("""
            SELECT balance FROM accounts WHERE user_id=%s
        """, (user_id,))
        sender_balance = cursor.fetchone()

        if not sender_balance:
            print("❌ Sender account not found.")
            return

        if amount > sender_balance[0]:
            print("❌ Insufficient balance.")
            return

        # Step 4: Deduct sender balance
        cursor.execute("""
            UPDATE accounts
            SET balance = balance - %s
            WHERE user_id=%s
        """, (amount, user_id))

        # Step 5: Credit receiver
        cursor.execute("""
            UPDATE accounts
            SET balance = balance + %s
            WHERE user_id=%s
        """, (amount, receiver_id))

        # Step 6: Record transaction
        cursor.execute("""
            INSERT INTO transactions (user_id, amount, type)
            VALUES (%s, %s, %s)
        """, (user_id, amount, f"Transfer to {receiver_username}"))

        conn.commit()

        print("✅ Transfer successful!")
        print(f"💸 ₹{amount} sent to {receiver_username}")

    except Exception as e:
        conn.rollback()
        print("❌ Transfer failed:", e)

    finally:
        cursor.close()
        conn.close()


# -----------------------------------------
# VIEW ACCOUNT INFO
# -----------------------------------------
def view_account_info(user_id):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)

    try:
        cursor.execute("""
            SELECT account_number, account_type, balance
            FROM accounts
            WHERE user_id=%s
        """, (user_id,))
        account = cursor.fetchone()

        if not account:
            print("❌ Account not found.")
            return

        print("\n" + "="*40)
        print("🏦 ACCOUNT DETAILS")
        print("="*40)
        print(f"🔢 Account Number : {account[0]}")
        print(f"🏷 Account Type   : {account[1]}")
        print(f"💰 Balance        : ₹{account[2]}")
        print("="*40)

    finally:
        cursor.close()
        conn.close()



# -----------------------------------------
# CHANGE MPIN
# -----------------------------------------
def change_mpin(user_id):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)

    try:
        old_pin = input("🔐 Enter current MPIN: ")

        cursor.execute("""
            SELECT pin FROM cards
            WHERE user_id=%s AND card_type='Debit'
        """, (user_id,))
        card = cursor.fetchone()

        if not card:
            print("❌ Debit card not found.")
            return

        if old_pin != card[0]:
            print("❌ Incorrect current MPIN.")
            return

        while True:
            new_pin = input("🔐 Enter new 4-digit MPIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                break
            else:
                print("❌ MPIN must be exactly 4 digits.")

        cursor.execute("""
            UPDATE cards
            SET pin=%s
            WHERE user_id=%s AND card_type='Debit'
        """, (new_pin, user_id))

        conn.commit()
        print("✅ MPIN updated successfully.")

    except Exception as e:
        conn.rollback()
        print("❌ Error changing MPIN:", e)

    finally:
        cursor.close()
        conn.close()


# -----------------------------------------
# REGISTER NEW CREDIT CARD
# -----------------------------------------
def register_new_credit_card(user_id):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)

    try:
        cvv = str(random.randint(100, 999))

        cursor.execute("""
            INSERT INTO cards (user_id, card_type, pin, cvv)
            VALUES (%s, %s, %s, %s)
        """, (user_id, "Credit", "0000", cvv))

        conn.commit()
        print("✅ New Credit Card registered successfully.")

    except Exception as e:
        conn.rollback()
        print("❌ Error registering credit card:", e)

    finally:
        cursor.close()
        conn.close()


# -----------------------------------------
# VIEW LAST 5 TRANSACTIONS
# -----------------------------------------
def view_transactions(user_id):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)

    try:
        cursor.execute("""
            SELECT amount, type, created_at
            FROM transactions
            WHERE user_id=%s
            ORDER BY created_at DESC
            LIMIT 5
        """, (user_id,))

        transactions = cursor.fetchall()

        if not transactions:
            print("📭 No transactions found.")
            return

        print("\n📊 Last 5 Transactions:")
        for t in transactions:
            print(f"{t[2]} | 💳 {t[1]} | ₹{t[0]}")

    finally:
        cursor.close()
        conn.close()