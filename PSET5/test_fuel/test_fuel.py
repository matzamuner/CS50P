import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("50/100") == 50
    assert convert("3/100") == 3
    assert convert("100/100") == 100
    assert convert("0/100") == 0
    with pytest.raises(ValueError):
        convert("101/100")
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
