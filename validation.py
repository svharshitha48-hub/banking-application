def validate_mobile(mobile):
    return len(mobile) == 10 and mobile.isdigit()

def validate_aadhar(aadhar):
    return len(aadhar) == 12 and aadhar.isdigit()