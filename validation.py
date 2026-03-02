# validation.py

import re

# -----------------------------
# Username Validation
# -----------------------------

def validate_username(username):
    """
    Username Rules:
    - Must start with a letter
    - Can contain letters and numbers only
    - Minimum 4 characters
    """

    if len(username) < 4:
        print("❌ Username must be at least 4 characters long.")
        return False

    pattern = r'^[A-Za-z][A-Za-z0-9]*$'

    if not re.match(pattern, username):
        print("❌ Username must start with a letter and contain only letters & numbers.")
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