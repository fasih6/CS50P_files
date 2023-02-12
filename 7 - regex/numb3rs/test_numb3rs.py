from numb3rs import validate

import pytest


def test_zero_division():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True
    assert validate("275.3.6.28") == False
    assert validate("cat") == False
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False
    assert validate("255.255.255.255") == True
    assert validate("255.1000.1000.1000") == False
    assert validate("1.1.1.1") == True
    assert validate("cat") == False
    assert validate("1.230.1000.0") == False
    assert validate("1.300.500.700") == False



