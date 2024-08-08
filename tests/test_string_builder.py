from lib.string_builder import *

def test_returns_empty_string_if_nothing_added():
    string = StringBuilder()
    assert string.output() == ""

def test_returns_given_string():
    string = StringBuilder()
    string.add("Hello, Andy!")
    # result = string.output()
    assert string.output() == "Hello, Andy!"

def test_check_length_of_given_string():
    string = StringBuilder()
    string.add("Hello")
    result = string.size()
    assert result == 5


def test_adds_multiple_strings_and_returns_in_one_string():
    string = StringBuilder()
    string.add("Hello, Andy!")
    string.add(" ")
    string.add("How are you?")
    result = string.output()
    assert result == "Hello, Andy! How are you?"

def test_returns_length_of_two_added_strings():
    string = StringBuilder()
    string.add("Hello")    
    string.add(" ")    
    string.add("World")
    result = string.size()
    assert result == 11