import random
import string
def password_generator():
    length = int(input("Enter the desired password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return f"Generated Password: {password}"
print(password_generator())