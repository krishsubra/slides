from mymod_1 import is_anagram

def test_anagram():
    assert is_anagram("elvis", "lives")
    assert is_anagram("silent", "listen")
    assert not is_anagram("one", "two")
