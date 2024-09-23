from seasons import convert
import pytest

def test_convert():
    assert convert("2003-05-13") == "eleven million, one hundred seventy-seven thousand, two hundred eighty"
