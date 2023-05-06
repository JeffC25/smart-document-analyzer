from database import *

def test_answer():
    assert renameFile("invalid", "valid", "name") == "failed"
    assert renameFile("username", "valid", "anotherName") == "success"
    assert renameFile("username", "valid", "invalid") == "failed"
    assert renameFile("invalid", "invalid", "invalid") == "failed"

    assert deleteFile("invalid", "valid") == "failed"
    assert deleteFile("username", "valid") == "success"
    assert deleteFile("invalid", "invalid") == "failed"