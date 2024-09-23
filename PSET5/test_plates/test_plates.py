from plates import is_valid


def test_isvalid_valid():
    assert is_valid("ABCDEG") == True
    assert is_valid("ABC123") == True
    assert is_valid("abcdeg") == True

def test_isvalid_invalid():
    assert is_valid("123456") == False
    assert is_valid("ABCDEGG") == False
    assert is_valid("s") == False
    assert is_valid("ABC000") == False
    assert is_valid("ABCD&G") == False
    assert is_valid("AB5DEG") == False


