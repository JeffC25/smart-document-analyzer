from file import *

def test_answer():
    assert uploadFile("valid", "valid") == "success"
    assert uploadFile("invalid", "invalid") == "failed"
    assert uploadFile(1, 2) == "failed"
