from lib.counter import *

def test_to_check_method_counts_correctly():
    count = Counter()
    count.add(5)
    result = count.report()
    assert result == "Counted to 5 so far."

def test_to_check_it_counts_zero():
    count = Counter()
    count.add(0)
    result = count.report()
    assert result == "Counted to 0 so far."

def test_to_check_it_add_negative_numbers():
    count = Counter()
    count.add(-5)
    result = count.report()
    assert result == "Counted to -5 so far."

def test_to_check_it_adds_together_numbers():
    count = Counter()
    count.add(-5 + 10)
    result = count.report()
    assert result == "Counted to 5 so far."