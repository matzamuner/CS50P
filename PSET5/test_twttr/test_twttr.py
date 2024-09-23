from twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("aeiou") == ""
    assert shorten("12345") == "12345"
    assert shorten("") == ""
    assert shorten(".,.,;") == ".,.,;"
