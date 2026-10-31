import pytest

from password_tool.rules import (
    has_min_length,
    has_uppercase,
    has_lowercase,
    has_digit,
    has_symbol,
    is_not_common_password, 
    password_loader
)

# has_min_length
def test_min_length_exactly_12_passes():
    assert has_min_length("a" * 12) is True

def test_min_length_11_fails():
    assert has_min_length("a" * 11) is False

def test_min_length_empty_string():
    assert has_min_length("") is False


# has_uppercase
def test_uppercase_present():
    assert has_uppercase("abcD") is True

def test_uppercase_missing():
    assert has_uppercase("abcd") is False

def test_uppercase_empty_string():
    assert has_uppercase("") is False


# has_lowercase
def test_lowercase_present():
    assert has_lowercase("ABCd") is True

def test_lowercase_missing():
    assert has_lowercase("ABCD") is False

def test_lowercase_empty_string():
    assert has_lowercase("") is False


# has_digit
def test_digit_present():
    assert has_digit("abc1") is True

def test_digit_missing():
    assert has_digit("abc") is False

def test_digit_empty_string():
    assert has_digit("") is False


# has_symbol
def test_symbol_present():
    assert has_symbol("abc!") is True

def test_symbol_missing():
    assert has_symbol("abc123") is False

def test_symbol_empty_string():
    assert has_symbol("") is False

def test_common_password_rejected():
    assert is_not_common_password("password") is False

def test_common_password_case_insensitive():
    assert is_not_common_password("PASSWORD") is False

def test_uncommon_password_passes():
    assert is_not_common_password("Xk9!mQ2vLp") is True

def test_empty_string_passes_common_check():
    assert is_not_common_password("") is True

def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        password_loader("does_not_exist.txt")