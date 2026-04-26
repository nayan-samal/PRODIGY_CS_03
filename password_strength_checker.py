import re


COMMON_PASSWORDS = {
    "123456", "12345678", "password", "admin", "hello123",
    "qwerty", "abc123", "password123", "welcome", "pizza"
}


def check_password_strength(password):
    score = 0
    feedback = []

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This is a very common password. Choose something unique.")
        return "Very Weak", feedback

    # Length check
    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters required)")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good length")
    else:
        score += 1
        feedback.append("Decent length, consider making it longer")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Contains uppercase letters")
    else:
        feedback.append("Add uppercase letters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Contains lowercase letters")
    else:
        feedback.append("Add lowercase letters")

    # Numbers
    if re.search(r"\d", password):
        score += 1
        feedback.append("Contains numbers")
    else:
        feedback.append("Add numbers")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("Contains special characters")
    else:
        feedback.append("Add special characters")

    # Spaces
    if " " in password:
        feedback.append("Avoid using spaces in password")

    # Repeated characters
    if re.search(r"(.)\1\1", password):
        feedback.append("Avoid repeating characters excessively")

    # Strength rating
    if score <= 3:
        strength = "Weak"
    elif score <= 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


# User Input
password = input("Enter your password: ")

strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)
print("\nFeedback:")

for tip in feedback:
    print("-", tip)