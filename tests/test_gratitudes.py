from lib.gratitudes import *

"""
returns none if no gratitudes are added
"""

def test_return_no_grattitudes_when_none_added():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

"""
Returns one gratitude
"""

def test_returns_one_grattitude():
    gratitudes = Gratitudes()
    gratitudes.add("My dogs")
    assert gratitudes.format() == "Be grateful for: My dogs"

"""
Returns multiple gratitudes when added
"""

def test_returns_multiple_grattitudes_when_added():
    gratitudes = Gratitudes()
    gratitudes.add("My dogs")
    gratitudes.add("My partner")
    gratitudes.add("Football")
    assert gratitudes.format() == "Be grateful for: My dogs, My partner, Football"


def test_add_duplicate_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("My dogs")
    gratitudes.add("My dogs")
    assert gratitudes.format() == "Be grateful for: My dogs, My dogs"

def test_add_empty_string():
    gratitudes = Gratitudes()
    gratitudes.add("")
    assert gratitudes.format() == "Be grateful for: "
