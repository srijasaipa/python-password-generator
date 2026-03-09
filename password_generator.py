import secrets
import string
import math

def generate_password(length=12):
    """Generate a secure random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def calculate_entropy(password):
    """Calculate entropy (password strength)."""
    char_pool = 0

    if any(c.islower() for c in password):
        char_pool += 26
    if any(c.isupper() for c in password):
        char_pool += 26
    if any(c.isdigit() for c in password):
        char_pool += 10
    if any(c in string.punctuation for c in password):
        char_pool += len(string.punctuation)

    entropy = math.log2(char_pool ** len(password))
    return entropy


print("===== Secure Password Generator =====")

while True:
    length = int(input("Enter desired password length: "))

    password = generate_password(length)
    entropy = calculate_entropy(password)

    print("\nGenerated Password:", password)
    print("Password Entropy:", round(entropy, 2), "bits")

    if entropy < 50:
        print("Weak password! Try a longer password.")
    elif entropy < 80:
        print("Moderate password. Could be stronger.")
    else:
        print("Strong password! Very secure.")

    user_choice = input("Are you happy with this password? (yes/no): ").lower()

    if user_choice == "yes":
        print("Password finalized.")
        break
    else:
        print("Generating a new password...\n")