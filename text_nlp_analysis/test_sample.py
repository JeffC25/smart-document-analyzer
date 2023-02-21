from nlp import *

def test_answer():
    assert convertDocument("valid", "valid", "valid") == "success"
    assert convertDocument("does not exist", "bad format", "bad format") == "failed"
    assert convertDocument("valid", "bad format", "bad format") == "failed"
    assert convertDocument("valid", "valid", "bad format") == "failed"
    assert convertDocument("valid", "bad format", "valid") == "failed"
