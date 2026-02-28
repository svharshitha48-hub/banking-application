# validation.py

import re

# -----------------------------
# Username Validation
# -----------------------------
def validate_username(username: str) -> bool:
    """
    Username must:
    - Be 3–20 characters
    - Contain only letters and numbers
    """
    if not username:
        print("Username cannot be empty.")
        return False

    if not re.match(r"^[A-Za-z0-9]{3,20}$", username):
        print("Username must be 3-20 characters, letters and numbers only.")
        return False

    return True


# -----------------------------
# Mobile Number Validation
# -----------------------------
def validate_mobile(mobile: str) -> bool:
    """
    Mobile must:
    - Be exactly 10 digits
    """
    if not re.match(r"^[0-9]{10}$", mobile):
        print("Mobile number must be exactly 10 digits.")
        return False

    return True


# -----------------------------
# Aadhar Validation
# -----------------------------
def validate_aadhar(aadhar: str) -> bool:
    """
    Aadhar must:
    - Be exactly 12 digits
    """
    if not re.match(r"^[0-9]{12}$", aadhar):
        print("Aadhar must be exactly 12 digits.")
        return False

    return True


# -----------------------------
# Amount Validation
# -----------------------------
def validate_amount(amount: float) -> bool:
    """
    Transfer amount must:
    - Be positive
    - Not zero
    """
    if amount <= 0:
        print("Amount must be greater than zero.")
        return False

    return True


# -----------------------------
# PIN Validation
# -----------------------------
def validate_pin(pin: str) -> bool:
    """
    PIN must:
    - Be exactly 4 digits
    """
    if not re.match(r"^[0-9]{4}$", pin):
        print("PIN must be exactly 4 digits.")
        return False

    return True