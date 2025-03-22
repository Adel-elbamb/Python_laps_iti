import re  

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name and not name.isdigit():  
            return name
        print("Error: Please enter a valid name (not empty or a number).")

def get_valid_email():
    while True:
        email = input("Enter your email: ").strip()
        if is_valid_email(email):  
            return email
        print("Error: Please enter a valid email address.")


name = get_valid_name()
email = get_valid_email()

print("\nUser Details:")
print(f"Name: {name}")
print(f"Email: {email}")
