import argparse
import sys

from .checker import PasswordChecker
from .generator import generate_password
from .rules import (
    MIN_LENGTH,
    has_min_length,
    has_uppercase,
    has_lowercase,
    has_digit,
    has_symbol,
    is_not_common_password,
)

DEFAULT_RULES = [
    ("needs at least 12 characters", has_min_length),
    ("needs an uppercase letter", has_uppercase),
    ("needs a lowercase letter", has_lowercase),
    ("needs a single digit", has_digit),
    ("needs a symbol", has_symbol),
    ("is too common", is_not_common_password),
]


def build_parser() -> argparse.ArgumentParser:
    """Describe the commands and options the tool accepts."""
    parser = argparse.ArgumentParser(
        prog="password_tool",
        description="Check password strength or generate a secure password.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    check = subparsers.add_parser("check", help="Score a password")
    check.add_argument("password", help="The password to check")

    generate = subparsers.add_parser("generate", help="Generate a password")
    generate.add_argument(
        "--length",
        type=int,
        default=16,
        help=f"Password length (minimum {MIN_LENGTH}, default 16)",
    )
    return parser


def run_check(password: str) -> int:
    """Print the score and failed rules. Return 0 if all rules pass, else 1."""
    result = PasswordChecker(DEFAULT_RULES).check(password)
    print(f"Score: {result['score']}/{len(DEFAULT_RULES)}")
    for reason in result["reasons"]:
        print(f"- {reason}")
    return 1 if result["reasons"] else 0


def run_generate(length: int) -> int:
    """Print a generated password. Return 1 if the length is invalid."""
    try:
        print(generate_password(length))
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    """Parse the command line and run the chosen command."""
    args = build_parser().parse_args(argv)
    if args.command == "check":
        return run_check(args.password)
    return run_generate(args.length)


if __name__ == "__main__":
    sys.exit(main())