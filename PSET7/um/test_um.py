from um import count

def test_count_true():
    assert count("lets um go") == 1
    assert count("um?") == 1
    assert count("Um um um") == 3

def test_count_false():
    assert count("lets go") == 0
    assert count("?") == 0
    assert count("") == 0

def test_count_separation():
    assert count("yummy") == 0
    assert count("scum") == 0
    assert count("tummy") == 0
