from output_generator import *

def test_answer():
    assert downloadFile("valid", "valid") == "success"
    assert downloadFile("invalid", "invalid") == "failed"
    assert downloadFile("valid", "invalid") == "failed"

    assert downloadFolder("valid", "valid") == "success"
    assert downloadFolder("invalid", "invalid") == "failed"
    assert downloadFolder("valid", "invalid") == "failed" 