MIN_LENGTH = 12
symbols = "! # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~"

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

