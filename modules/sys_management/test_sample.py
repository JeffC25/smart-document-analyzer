from sys_management import *

def test_answer():
    assert changePassword("valid", "correct", "valid") == "success"
    assert changePassword("invalid", "incorrect", "valid") == "failed"
    assert changePassword("valid", "correct", "invalid") == "failed"

    assert deleteUser('username', 'password') == "success"
    assert deleteUser('username', 'wrong') == "failed"
    assert deleteUser('wrong', 'password') == "failed"
    assert deleteUser('wrong', 'wrong') == "failed"

    assert updateUser('username', 'password') == "success"
    assert updateUser('username', 'wrong') == "failed"
    assert updateUser('wrong', 'password') == "failed"
    assert updateUser('wrong', 'wrong') == "failed"