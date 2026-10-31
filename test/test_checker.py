import pytest

from password_tool.checker import PasswordChecker
from password_tool.rules import (
    has_min_length,
    has_uppercase,
    has_lowercase,
    has_digit,
    has_symbol,
)

LENGTH_MSG = "needs at least 12 characters"


@pytest.fixture
def checker():
    rules_list = [
        (LENGTH_MSG, has_min_length),
        ("needs an uppercase letter", has_uppercase),
        ("needs a lowercase letter", has_lowercase),
        ("needs a single digit", has_digit),
        ("needs a symbol", has_symbol),
    ]
    return PasswordChecker(rules_list)


def test_strong_password(checker):
    result = checker.check("Str0ng!Passw0rd")
    assert result["score"] == 5
    assert result["reasons"] == []


def test_weak_password(checker):
    result = checker.check("abc")
    assert result["score"] == 1
    assert len(result["reasons"]) == 4


def test_empty_string(checker):
    result = checker.check("")
    assert result["score"] == 0
    assert len(result["reasons"]) == 5


def test_specific_reason_appears(checker):
    result = checker.check("pasSword!")
    assert LENGTH_MSG in result["reasons"]


def test_no_carry_over_between_calls(checker):
    first = checker.check("pasSword!")
    second = checker.check("pasSword!")
    assert first == second