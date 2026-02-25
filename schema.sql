CREATE DATABASE banking_app;
USE banking_app;
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100),
    address VARCHAR(255),
    aadhar VARCHAR(20),
    mobile VARCHAR(15),
    balance DECIMAL(10,2) DEFAULT 10000
);
CREATE TABLE cards (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    card_type VARCHAR(20),
    pin VARCHAR(4),
    cvv VARCHAR(3),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE TABLE beneficiaries (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    name VARCHAR(100),
    account_no VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE TABLE transactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    amount DECIMAL(10,2),
    type VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);