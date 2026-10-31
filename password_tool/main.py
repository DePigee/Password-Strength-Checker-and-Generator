from .rules import has_min_length, has_uppercase, has_lowercase, has_digit, has_symbol

def main():
    password = "pasSword!"
    
    has_min_length(password)
    has_uppercase(password)
    has_uppercase(password)
    has_lowercase(password)
    has_digit(password)
    has_symbol(password)


if __name__ == "__main__":
    main()