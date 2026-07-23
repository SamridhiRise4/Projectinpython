import random
import string
import pyperclip
from datetime import datetime


# ------------------------------
# Generate Password
# ------------------------------
def generate_password(length,
                      upper,
                      lower,
                      numbers,
                      symbols,
                      avoid_confusing):

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()_-+=<>?/{}[]"

    confusing = "O0Il1"

    characters = ""

    if upper:
        characters += uppercase

    if lower:
        characters += lowercase

    if numbers:
        characters += digits

    if symbols:
        characters += special

    if avoid_confusing:
        for char in confusing:
            characters = characters.replace(char, "")

    if len(characters) == 0:
        return None

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


# ------------------------------
# Password Strength
# ------------------------------
def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"


# ------------------------------
# Save Password
# ------------------------------
def save_password(password):

    with open("passwords.txt", "a") as file:

        file.write(
            f"{datetime.now()}  -->  {password}\n"
        )

    print("Password saved successfully.")


# ------------------------------
# Copy Password
# ------------------------------
def copy_password(password):

    pyperclip.copy(password)

    print("Password copied to clipboard.")


# ------------------------------
# Menu
# ------------------------------
while True:

    print("\n")
    print("=" * 50)
    print("        PASSWORD GENERATOR")
    print("=" * 50)

    print("1. Generate Password")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        try:

            length = int(input("Password Length: "))

        except:

            print("Invalid Length")
            continue

        upper = input("Include Uppercase? (y/n): ").lower() == "y"

        lower = input("Include Lowercase? (y/n): ").lower() == "y"

        numbers = input("Include Numbers? (y/n): ").lower() == "y"

        symbols = input("Include Special Characters? (y/n): ").lower() == "y"

        avoid = input("Avoid Confusing Characters? (y/n): ").lower() == "y"

        total = int(input("How many passwords do you want?: "))

        print("\nGenerated Passwords\n")

        for i in range(total):

            password = generate_password(
                length,
                upper,
                lower,
                numbers,
                symbols,
                avoid
            )

            if password is None:
                print("Select at least one character type.")
                break

            print(f"{i+1}. {password}")

            print("Strength:", check_strength(password))

            save = input("Save this password? (y/n): ")

            if save.lower() == "y":
                save_password(password)

            copy = input("Copy to Clipboard? (y/n): ")

            if copy.lower() == "y":
                copy_password(password)

            print("-" * 40)

    elif choice == "2":

        print("Thank You!")

        break

    else:

        print("Invalid Choice")

        
