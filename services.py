from db import get_connection
import random

def register_user(username, address, aadhar, mobile):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (username, address, aadhar, mobile)
        VALUES (%s, %s, %s, %s)
    """, (username, address, aadhar, mobile))

    user_id = cursor.lastrowid

    # Create Debit Card
    cursor.execute("""
        INSERT INTO cards (user_id, card_type, pin, cvv)
        VALUES (%s, %s, %s, %s)
    """, (user_id, "Debit", "1234", str(random.randint(100,999))))

    # Create Credit Card
    cursor.execute("""
        INSERT INTO cards (user_id, card_type, pin, cvv)
        VALUES (%s, %s, %s, %s)
    """, (user_id, "Credit", "5678", str(random.randint(100,999))))

    conn.commit()
    conn.close()

    print("Registration successful. Please login.")



def login(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()

    conn.close()
    return user

def transfer_fund(user_id, amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET balance = balance - %s WHERE id = %s", (amount, user_id))

    cursor.execute("""
        INSERT INTO transactions (user_id, amount, type)
        VALUES (%s, %s, %s)
    """, (user_id, amount, "Debit"))

    conn.commit()
    conn.close()