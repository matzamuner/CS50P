from working import convert
import pytest

def test_working():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 17 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 17:60 PM")
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
