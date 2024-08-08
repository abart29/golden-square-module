import pytest
from lib.present import *

"""
Test to instantiate object
"""
def test_instantiate_object_from_class():
    present = Present()
    assert present.contents == None

"""
Test to see if content has been added to object using wrap method
"""
def test_to_return_contents_from_wrap():
    present = Present()
    present.wrap("Football")
    assert present.contents == "Football"

"""
Test to see if content has been added to object using wrap method
**wrap and then unwrap**
"""
def test_to_return_contents_after_adding_present():
    present = Present()
    present.wrap("Football")
    assert present.unwrap() == "Football"

"""
Test to raise exception error if no contents have been added so there for nothing can be wrapped
"""

def test_raise_exception_error_if_contents_is_none():
    item = Present()
    with pytest.raises(Exception) as err:
        item.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."

"""
test to raise exception error if present/contents has already added/been wrapped. 
***try to wrap the same contents twice you get error message*** 
"""

def test_to_raise_exception_error_if_present_has_already_been_wrapped():
    item = Present()
    item.wrap("Football")
    with pytest.raises(Exception) as err:
        item.wrap("Football")
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

"""
Test to make sure currently wrapped present isn't replaced by wrap
"""
def test_first_wrapped_value_is_unchanged():
    present = Present()
    present.wrap("Football")
    with pytest.raises(Exception) as e:
        present.wrap("PS5")
    assert present.unwrap() == "Football"

"""
"""
def test_first_wrapped_value_throws_error_despite_new_present_being_added():
    present = Present()
    present.wrap("Football")
    with pytest.raises(Exception) as e:
        present.wrap("PS5")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."