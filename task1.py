import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special):
    character_pool = ""
    
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_numbers:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("At least one character type must be selected")
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired password length: "))
    
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    try:
        password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special)
        print("Generated password:",password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
