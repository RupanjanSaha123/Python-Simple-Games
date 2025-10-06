import random
import string

def generate_password():
    try:
        length = int(input("Enter the length of the password: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number for the length.")
        return

    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower()
    include_special = input("Include special characters? (y/n): ").strip().lower()
    include_numbers = input("Include numbers? (y/n): ").strip().lower()

    if length < 4 :
        print("Password length should be at least 4 characters.")
        return
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase == 'y' else ''
    special = string.punctuation if include_special == 'y' else ''
    numbers = string.digits if include_numbers == 'y' else ''

    characters = lower + upper + special + numbers

    if not characters:
        print("You must select at least one character set.")
        return

    required_chars = []
    if include_uppercase == 'y':
        required_chars.append(random.choice(upper))
    if include_special == 'y':
        required_chars.append(random.choice(special))
    if include_numbers == 'y':
        required_chars.append(random.choice(numbers))

    # Ensure at least one lowercase character is included
    required_chars.append(random.choice(lower))

    remaining_length = length - len(required_chars)
    
    # If length is too small for all required types, adjust
    if remaining_length < 0:
        print("Warning: Length is too short to include all selected character types. Adjusting password.")
        remaining_length = 0
        required_chars = required_chars[:length]


    password_chars = required_chars + random.choices(characters, k=remaining_length)
    random.shuffle(password_chars)
    
    password = "".join(password_chars)
    print(f"Generated password: {password}")


generate_password()