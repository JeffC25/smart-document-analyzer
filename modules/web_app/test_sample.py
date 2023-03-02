from web import *

def test_answer():
    assert searchFile("valid") == "success"
    assert searchFile("invalid") == "failed"
    
    assert searchFolder("valid") == "success"
    assert searchFolder("invalid") == "failed"

    assert logout() == "success"