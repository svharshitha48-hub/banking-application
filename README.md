Project Overview:
This is a console-based banking system developed using Python and MySQL.
It supports Registration, Login, Account Info, Fund Transfer, Beneficiary Management,
Card Management, and Transaction Recording.
Technologies Used:
- Python 3
- MySQL
- mysql-connector-python
- Git
- Linux Terminal
Project Structure:
main.py – Entry point
db.py – Database connection
services.py – Business logic
validation.py – Input validations
menu.py – Menu display
schema.sql – Database schema
README.md – Documentation
Database Setup:
1. Start MySQL: sudo service mysql start
2. Login: mysql -u root -p
3. Create DB:
CREATE DATABASE banking_app;
USE banking_app;
4. Run schema:
mysql -u root -p banking_app < schema.sql
Tables Created:
- users
- cards
- beneficiaries
- transactions
Installation:
pip install mysql-connector-python
Run Project:
cd Harshitha_Banking_Application
python3 main.py
Registration Flow:
User enters Username, Address, Aadhar, Mobile.
System auto-creates:
- 1 Debit Card
- 1 Credit Card
Default balance = 10000
Login Flow:
User enters username.
If found → menu shown.
If not found → error message.
User Menu Options:
1. View Account Info
2. Add Beneficiary
3. Transfer Fund
4. Change MPIN
5. Register Credit Card
6. Logout
Fund Transfer:
- Deducts balance
- Creates transaction entry
- Updates database in real-time
Card Management:
Each user gets:
- Debit Card (PIN + CVV)
- Credit Card (PIN + CVV)
User can change MPIN.
Transaction Recording:
Stored in transactions table with:
- user_id
- amount
- type
- timestamp
Python Concepts Used:
- Modular programming
- Functions
- MySQL integration
- Exception handling
- Code reusability
- Foreign keys
- Input validation
- Random generation
Git Usage:
git add .
git commit -m "Update"
git push origin main
Debugging:
python3 -m pdb main.py
or
import pdb; pdb.set_trace()
Enhancements Possible:
- Add password login
- Add insufficient balance validation
- Add transaction history
- Add logging
- Convert to OOP
- Add REST API
Conclusion:
This project demonstrates backend development, database integration,
modular programming, and real-world banking workflow simulation.
Author:
Harshitha