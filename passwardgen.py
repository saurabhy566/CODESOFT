import random
import string

def passward_gen(length):
   
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase + uppercase + digits + special_characters
    passward = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    passward +=random.choices(all_characters, k=length - 4)

    random.shuffle(passward)
    return ''.join(passward)
try:
    length = int(input("Enter the length of the password (minimum 4): "))
    
    if length < 4:
        print("Password length should be at least 4 .")
    else:
        print("Generated Password:", passward_gen(length))
        
except ValueError:
    print("Please enter a valid integer for the password length.")
