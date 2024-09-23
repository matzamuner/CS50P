from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(5) == 5
    with pytest.raises(ValueError):
        assert jar.deposit(13)


def test_withdraw():
    jar = Jar()
    assert jar.deposit(5) == 5
    assert jar.withdraw(2) == 3
