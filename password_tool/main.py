from .rules import has_min_length, has_uppercase, has_lowercase, has_digit, has_symbol
from .checker import PasswordChecker

def main():
    password = "pasSword!"
    rules_list = [("needs at least 12 characters", has_min_length),("needs an uppercase letter", has_uppercase),
                  ("needs a lowercase letter", has_lowercase), ("needs a single digit", has_digit), 
                  ("needs a symbol", has_symbol)
                ]

    password_checker = PasswordChecker(rules_list)
    print(password_checker.check(password))

if __name__ == "__main__":
    main()