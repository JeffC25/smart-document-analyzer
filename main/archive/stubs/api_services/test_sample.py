from services import *

def test_answer():
    assert checkQuota("example") == 100
    assert keygen("example") == "apikey"