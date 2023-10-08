import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

# Generate a 12-character password
password = generate_password(12)
print(password)