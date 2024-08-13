from twttr import shorten

def test_shorten():
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("Ahmet Nuri Aydemir") == "hmt Nr ydmr"
    assert shorten("Wrong") == "Wrong"
