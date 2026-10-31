from .rules import MIN_LENGTH
import secrets, string


def generate_password(length: int = 16) -> str:
    if(length < MIN_LENGTH):
        raise ValueError(f"Password is only {length} long when it needs to be at least {MIN_LENGTH} long")
    password_chars = [secrets.choice(string.digits), secrets.choice(string.ascii_uppercase), secrets.choice(string.ascii_lowercase), secrets.choice(string.punctuation)]

    pool = (
         string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + string.punctuation
    )

    for i in range(length - len(password_chars)):
        password_chars.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)
    
