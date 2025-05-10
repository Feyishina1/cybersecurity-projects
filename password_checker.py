import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Less than 8 characters"
    if not re.search(r"[A-Z]", password):
        return "Weak: No uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Weak: No lowercase letter"
    if not re.search(r"\d", password):
        return "Weak: No digit"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: No special character"
    return "Strong password"

password = input("Enter a password to check: ")
print(check_password_strength(password))
