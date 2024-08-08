from lib.check_codeword import *

"""
if code word is correct
return "Correct! Come in."
"""
def test_to_check_if_codeword_is_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

"""
if code word has the right first and last letter
return "Close, but nope."
"""

def test_to_check_if_codeword_is_nearly_correct():
    result = check_codeword("hope")
    assert result == "Close, but nope."

"""
if code word is wrong
return "WRONG!"
"""

def test_to_check_for_incorrect_codeword():
    result = check_codeword("World")
    assert result == "WRONG!"

"""
if the codeword has right first letter but wrong last one. 
Return "WRONG!"
"""

def test_with_right_first_letter_and_wrong_last_letter():
    result = check_codeword("hat")
    assert result == "WRONG!"

"""
if the codeword has right last letter but wrong first one. 
Return "WRONG!"
"""

def test_with_wrong_first_letter_and_right_last_letter():
    result = check_codeword("mouse")
    assert result == "WRONG!"