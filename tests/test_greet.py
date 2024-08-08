from lib.greet import *

def test_greet_returns_hello_with_given_name():
    result = greet("Andy")
    assert result == f"Hello, Andy!"