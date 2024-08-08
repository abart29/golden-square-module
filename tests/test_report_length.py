from lib.report_length import *

"""
Return correct length of string
"""

def test_to_return_length_of_string_hello():
    result = report_length("Lancashire")
    assert result == f"This string was 10 characters long."

"""
Returns 0 if no string is passed
"""

def test_to_report_zero_if_empty_string():
    result = report_length("")
    assert result == f"This string was 0 characters long."

"""
Returns length of string even if numbers
"""

def test_to_return_length_of_string_as_numbers():
    result = report_length("12")
    assert result == f"This string was 2 characters long."

"""
Returns length of both strings using concatenation 
"""

def test_to_return_length_with_concatenation():
    result = report_length("hello" + "world")
    assert result == f"This string was 10 characters long."

"""
Return length when string is uppercase
"""

def test_to_return_length_of_uppercase_string():
    result = report_length("HELLO")
    assert result == f"This string was 5 characters long."