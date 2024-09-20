import string
import secrets

def generate_password(length=12):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
# Example  usage
secure_password = generate_password(16)
print(f"Generated secure password: {secure_password}")
