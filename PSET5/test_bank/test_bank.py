from bank import value


def test_value():
    assert value("hello") == 0
    assert value("hello, how are you") == 0
    assert value("HELLO") == 0


def test_value_incorrect():
    assert value("..;,.;") == 100
    assert value("yo") == 100


def test_value_half():
    assert value("hi") == 20
    assert value("hi, how are you") == 20
    assert value("HI") == 20
