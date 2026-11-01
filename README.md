# Password Tool

A Python command-line tool that scores password strength and generates secure random passwords.

## Features

- Scores a password from 0 to 6 against six rules: minimum length, uppercase, lowercase, digit, symbol, and not a common password
- Reports exactly which rules a password failed
- Case-insensitive check against a list of commonly used passwords
- Generates random passwords with the `secrets` module, guaranteeing at least one uppercase letter, lowercase letter, digit, and symbol
- Simple CLI with `check` and `generate` commands

## Installation

```bash
git clone https://github.com/DePigee/Password-Strength-Checker-and-Generator.git
cd password-tool
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Requires Python 3.10 or newer.

## Usage

Check a password:

```bash
python -m password_tool.main check 'pasSword!'
```

```
Score: 4/6
- needs at least 12 characters
- needs a single digit
```

Generate a password (default length is 16, minimum is 12):

```bash
python -m password_tool.main generate --length 20
```

> **Note:** Wrap passwords in single quotes. Characters like `!` have special meaning in zsh and bash and can break double-quoted arguments.

The tool exits with code `0` on success and `1` if a check fails or the input is invalid.

## Running the tests

```bash
python -m pytest
```

The suite has [number] tests covering the rules, the checker, the generator, and the CLI.

## Project structure

```
password-tool/
├── password_tool/
│   ├── rules.py              # Pure rule functions and common-password loader
│   ├── checker.py            # PasswordChecker class
│   ├── generator.py          # Secure password generator
│   ├── cli.py                # argparse command-line interface
│   ├── main.py               # Entry point
│   └── commonpasswords.txt   # Common passwords list
├── test/                     # pytest test suite
├── requirements.txt
└── README.md
```

## Design decisions

**`secrets` instead of `random`.** Python's `random` module is predictable and meant for simulations. `secrets` uses the operating system's cryptographically secure randomness, which is the right choice for generating passwords. The final shuffle uses `secrets.SystemRandom()` for the same reason.

**Rules as independent pure functions.** Each rule takes a string and returns a boolean, with no side effects. That makes each one easy to test on its own. `PasswordChecker` takes a list of `(message, function)` pairs, so adding a rule is a one-line change.

**Fail loudly when the common-password list is missing.** If `commonpasswords.txt` can't be found, the loader raises a clear `FileNotFoundError` instead of returning an empty set. An empty set would silently turn the check off and let every password pass.

**Regression test for a real bug.** An early version of `PasswordChecker` kept its results on the instance, so calling `check()` twice on the same password doubled the score. Results are now built fresh on every call, and a test guards against it coming back.

**Generator guarantees every category.** Picking purely at random can occasionally miss a character type, which would fail the tool's own rules. The generator picks one character from each category first, fills the rest from the combined pool, then shuffles.

## Limitations and future work

- Passwords are passed as command-line arguments, so they can appear in shell history and the process list. A future version should read input with `getpass`.
- The common-password list is small ([number] entries). A real deployment would use a much larger list.
- Only ASCII punctuation counts as a symbol, and spaces do not.
- Strength is scored by counting rules passed, not by entropy or pattern detection (for example, `Password123!` style substitutions).