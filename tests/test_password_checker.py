import pytest
from lib.password_checker import *


"""
Checking if accepts a password longer than 8 characters
"""

def test_accepts_password_longer_than_eight_chars():
    password = PasswordChecker()
    assert password.check("123456789") == True

"""
Checking if func accepts special chars and longer than 8 characters
"""

def test_accepts_password_longer_than_eight_chars_containing_special_chars():
    password = PasswordChecker()
    assert password.check("123456!!!") == True

"""
Test for number less than 8 to return error
"""

def test_return_error_if_shorter_than_eight_chars():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("123456")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

"""
Test if takes different types of data - integers
"""

def test_passwordchecker_check_accepts_different_data_types():
    password = PasswordChecker()
    assert password.check("HelloAndy") == True