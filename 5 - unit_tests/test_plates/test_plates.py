from plates import is_valid

def test_1():
    assert is_valid("CS50") == True
def test_2():
    assert is_valid("ECTO88") == True
def test_3():
    assert is_valid("NRVOUS") == True
def test_4():
    assert is_valid("NRVOUSSS") == False
def test_5():
    assert is_valid("HELLO, WORLD") == False
def test_6():
    assert is_valid("GOODBYE") == False
def test_7():
    assert is_valid("CS05") == False
def test_8():
    assert is_valid("PI3.14") == False
def test_9():
    assert is_valid("H") == False
def test_10():
    assert is_valid("OUTATIME") == False
def test_11():
    assert is_valid("CS50P2") == False
    assert is_valid("CS50") == True
    assert is_valid("H") == False
    assert is_valid("PI3.14") == False
    assert is_valid("thisistoolong") == False
    assert is_valid("AAA22A") == False
    assert is_valid("CS05") == False
    assert is_valid("57EED") == False
    assert is_valid("32") == False
