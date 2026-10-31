import string
from pathlib import Path

MIN_LENGTH = 12
symbols = "! # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~"
COMMON_PASSWORDS_PATH = Path(__file__).parent / "commonpasswords.txt"


# Return True if the password has at least MIN_LENGTH characters.
def has_min_length(password: str) -> bool:
    return len(password) >= MIN_LENGTH

# Return True if the password has at least a uppercase character.
def has_uppercase(password: str) -> bool:
    for letter in password:
        if (letter.isupper()):
            return True  
    return False  

# Return True if the password has at least a lowercase character.
def has_lowercase(password: str) -> bool:
    for letter in password:
        if(letter.islower()):
            return True
    return False

# Return True if the password has at least a digits as a character.
def has_digit(password):
    for letter in password:
        if(letter.isdigit()):
            return True
    return False

# Return True if the password has at least a symbol as a character.
def has_symbol(password: str) -> bool:
    for letter in password:
        if(letter in symbols):
            return True
    return False

def password_loader(common_passwords_list):
    try:
        with open(common_passwords_list, "r") as file:
            passwords_list = file.read()
            passwords_list = passwords_list.splitlines("\n")
        return set(passwords_list)
    except FileNotFoundError:
        return []

def password_loader(file_path: str) -> set[str]:
    try:
        with open(file_path, "r") as file:
            passwords = set()
            for line in file:
                word = line.strip().lower()
                if word:
                    passwords.add(word)
        return passwords
    except FileNotFoundError:
        raise FileNotFoundError(f"Common passwords file not found: {file_path}")


COMMON_PASSWORDS = password_loader(COMMON_PASSWORDS_PATH)

def is_not_common_password(password: str) -> bool:
    """Return True if the password is not in the common passwords list."""
    return password.lower() not in COMMON_PASSWORDS

