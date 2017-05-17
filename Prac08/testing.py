__author__ = 'Tom Stanley'
"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from Prac07.car import Car


def repeat_string(s, n):
    """
    repeat string s, n times, with spaces in between
    """
    repeated_string = []
    for i in range(0, n):
        repeated_string.append(s)
    return " ".join(repeated_string).strip()


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def get_sentence(phrase):
    # phrase_length = len(phrase)
    # print(phrase[phrase_length - 1])
    if phrase[len(phrase) - 1] == '.':
        return phrase.capitalize()
    return phrase.capitalize() + '.'


def run_tests():
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"
    # assert test with custom message - used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    # Note that Car's __init__ function sets the fuel in one of two ways: using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    test_car = Car()
    assert test_car.fuel == 0
    assert get_sentence('hello') == 'Hello.'
    assert get_sentence('It is an ex parrot.') == 'It is an ex parrot.'
    assert get_sentence('this is a phrase') == 'This is a phrase.'

run_tests()
doctest.testmod()


# Important: start with a function header and just use pass as the body
# then add doctests so that:
# 'hello' -> ''Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (that's valid!)
# then write the body of the function so that the tests pass
