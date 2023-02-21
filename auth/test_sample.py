from auth import *

def test_answer():
    assert login('username', 'password') == "success"
    assert login('username', 'wrong') == "failed"
    assert login('wrong', 'password') == "failed"
    assert login('wrong', 'wrong') == "failed"