import pytest

from password_tool.checker import PasswordChecker
from password_tool.generator import generate_password
from password_tool.rules import (
    has_min_length,
    has_uppercase,
    has_lowercase,
    has_digit,
    has_symbol,
    is_not_common_password,
)


def test_generated_length_matches_request():
    for length in (12, 16, 32):
        assert len(generate_password(length)) == length


def test_default_length_is_16():
    assert len(generate_password()) == 16


def test_generated_password_passes_every_rule():
    for _ in range(100):
        password = generate_password()
        assert has_min_length(password) is True
        assert has_uppercase(password) is True
        assert has_lowercase(password) is True
        assert has_digit(password) is True
        assert has_symbol(password) is True


def test_too_short_raises_value_error():
    with pytest.raises(ValueError):
        generate_password(5)


def test_two_passwords_differ():
    assert generate_password() != generate_password()


def test_generated_password_scores_perfect_with_checker():
    checker = PasswordChecker([
        ("needs at least 12 characters", has_min_length),
        ("needs an uppercase letter", has_uppercase),
        ("needs a lowercase letter", has_lowercase),
        ("needs a single digit", has_digit),
        ("needs a symbol", has_symbol),
        ("is too common", is_not_common_password),
    ])
    for _ in range(100):
        result = checker.check(generate_password())
        assert result["score"] == 6
        assert result["reasons"] == []