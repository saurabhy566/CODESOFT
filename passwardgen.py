import random
import string

def passward_gen(length):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters
    
    # MAke sure the password has at least one character from each character set
    passward = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the remaining length with random choices from all characters
    passward +=random.choices(all_characters, k=length - 4)
    
    # Shuffle to avoid predictable patterns
    random.shuffle(passward)
    
    # Convert the list to a string and return
    return ''.join(passward)

# Prompt user for the desired password length
try:
    length = int(input("Enter the length of the password (minimum 4): "))
    
    if length < 4:
        print("Password length should be at least 4 .")
    else:
        # Generate and print the password
        print("Generated Password:", passward_gen(length))
        
except ValueError:
    print("Please enter a valid integer for the password length.")
