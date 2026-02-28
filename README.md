# 🏦 Harshitha Banking Application

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange.svg)
![CLI App](https://img.shields.io/badge/Interface-CLI-green.svg)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen.svg)

---

## 📌 Project Overview

The **Harshitha Banking Application** is a console-based banking system built using **Python and MySQL**.

This project simulates real-world banking operations such as:

- User Registration
- Login
- Account Creation
- Fund Transfer using MPIN
- Transaction Recording
- MPIN Change
- Credit Card Registration
- Transaction History Viewing

The project follows a **modular architecture**, separating business logic, database connection, and UI components.

---

# 🎯 Features Implemented

## 1️⃣ User Registration
- Collects:
  - Username
  - Address
  - Aadhar
  - Mobile Number
  - 4-digit MPIN
- Automatically:
  - Creates Savings Account
  - Generates Account Number
  - Allots Debit Card
  - Allots Credit Card
  - Initializes balance with ₹10,000

---

## 2️⃣ Login
- Login using username
- After login, user gets access to banking menu

---

## 3️⃣ View Account Information
Displays:
- Account Number
- Account Type
- Available Balance

---

## 4️⃣ Transfer Fund (Username-Based)
Steps:
1. Enter transfer amount
2. Enter MPIN for verification
3. Enter receiver username
4. System validates:
   - MPIN correctness
   - Receiver existence
   - Sufficient balance
5. Updates balances
6. Records transaction
7. Displays success message

This simulates **UPI-style username-based transfers**.

---

## 5️⃣ Change MPIN
- User enters current MPIN
- Validates correctness
- Allows setting new 4-digit MPIN
- Updates card record

---

## 6️⃣ Register New Credit Card
- Allows user to create additional credit card
- Auto-generates CVV
- Default PIN assigned

---

## 7️⃣ View Transaction History
- Displays last 5 transactions
- Shows:
  - Date
  - Type
  - Amount

---

# 🗂 Project Structure

```
Harshitha_Banking_Application/
│
├── main.py              # Entry point
├── services.py          # Business logic
├── db.py                # Database connection
├── menu.py              # Menu display
├── schema.sql           # Database tables
└── README.md            # Project documentation
```

---

# 🛠 Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- Modular Programming
- Exception Handling

---

# 🗄 Database Tables

### users
Stores user personal information.

### accounts
Stores account details and balance.

### cards
Stores debit and credit card details with MPIN.

### transactions
Stores transfer records.

---

# 🚀 How To Run The Project

## Step 1: Install Dependency

```bash
pip install mysql-connector-python
```

---

## Step 2: Setup MySQL Database

Login to MySQL:

```bash
mysql -u root -p
```

Create database:

```sql
CREATE DATABASE banking_app;
USE banking_app;
```

Exit MySQL.

---

## Step 3: Run Schema File

From project directory:

```bash
mysql -u root -p banking_app < schema.sql
```

---

## Step 4: Update Database Credentials

Open `db.py` and ensure:

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="banking_app"
)
```

---

## Step 5: Run Application

```bash
python3 main.py
```

---

# 📊 Evaluation Criteria Covered

✔ Use of Python Functions  
✔ Modular Code Structure  
✔ Code Reusability  
✔ Optimal Data Structures  
✔ Database Integration  
✔ Error Handling  
✔ Realistic Business Logic  
✔ Inline Comments  
✔ Proper Documentation  

---

# 🏦 Real-World Banking Concepts Implemented

- Account Creation
- Debit/Credit Card Allocation
- MPIN Verification
- Balance Deduction & Credit
- Transaction Logging
- Secure Fund Transfer Flow
- Prevent Self Transfer
- Insufficient Balance Handling

---

# 🔒 Security Implemented

- MPIN required for transfer
- MPIN required for change
- Balance validation
- Receiver validation
- Self-transfer restriction

---

# 📌 Assumptions

- Username is unique
- Initial account balance is ₹10,000
- Transfers occur within same banking system
- Console-based simulation

---

# 📈 Future Enhancements

- Daily transfer limit
- 3 wrong MPIN attempts lock
- Password-based login
- Transaction reference ID
- Admin dashboard
- Statement download

---

# 👩‍💻 Developed By

**Harshitha**  
Python Banking Application Project  

---

⭐ If you found this project useful, feel free to star the repository!