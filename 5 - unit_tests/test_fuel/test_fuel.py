from fuel import convert, gauge

import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_valueerror():
    with pytest.raises(ValueError):
        convert("5/4")

def test_float():
    with pytest.raises(ValueError):
        convert("5.5/4")
def test_str():
    with pytest.raises(ValueError):
        convert("cat")
def test_con():
    assert convert("1/4") == 25
    assert convert("4/4") == 100
def test_f():
    assert gauge(99) == "F"
def test_e():
    assert gauge(1) == "E"
def test_g1():
    assert gauge(67) == "67%"