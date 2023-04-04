def changePassword(username, oldPassword, newPassword):
    if not username == "valid" or not oldPassword == "correct":
        return "failed"
    if newPassword == "valid":
        return "success"
    return "failed"

def deleteUser(username, password):
    if username == "username" and password == "password":
        return "success"
    return "failed"

def updateUser(username, password):
    if username == "username" and password == "password":
        return "success"
    return "failed"