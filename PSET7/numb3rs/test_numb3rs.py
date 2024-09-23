from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.0") == True
    assert validate("10.10.10.10") == True
    assert validate("A.A.A.A") == False
    assert validate("1.1.2") == False
    assert validate(" . . . ") == False
    assert validate("255.255.255.255.255") == False
    assert validate("512.1.1.1") == False
    assert validate("1.512.1.1") == False
