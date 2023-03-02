from database import *

def test_answer():
    assert createFolder("username", "folder") == "success"
    assert createFolder("invalid","invalid") == "failed"
    assert createFolder(1,2) == "failed"

    assert moveFile("invalid", "valid", "valid") == "failed"
    assert moveFile("username", "valid", "valid") == "success"
    assert moveFile("username", "invalid", "invalid") == "failed"

    assert renameFile("invalid", "valid", "name") == "failed"
    assert renameFile("username", "valid", "anotherName") == "success"
    assert renameFile("username", "valid", "invalid") == "failed"
    assert renameFile("invalid", "invalid", "invalid") == "failed"

    assert deleteFile("invalid", "valid") == "failed"
    assert deleteFile("username", "valid") == "success"
    assert deleteFile("invalid", "invalid") == "failed"