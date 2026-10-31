from .rules import has_min_length, has_uppercase, has_lowercase, has_digit, has_symbol, is_not_common_password
from .checker import PasswordChecker
from .generator import generate_password
   
def main():
    password = "password!"
    rules_list = [("needs at least 12 characters", has_min_length),("needs an uppercase letter", has_uppercase),
                  ("needs a lowercase letter", has_lowercase), ("needs a single digit", has_digit), 
                  ("needs a symbol", has_symbol), ("is too common", is_not_common_password)
                ]
    
    password_checker = PasswordChecker(rules_list)
    print(password_checker.check(password))
    generate_password(20)
    
if __name__ == "__main__":
    main()