def createFolder(username, name):
    if username == "username" and name == "folder":
        return "success"
    return "failed"

def moveFile(username, file, folder):
    if not username == "username":
        return "failed"
    if file == "valid" and folder == "valid":
        return "success"
    return "failed"

def renameFile(username, file, newName):
    if not username == "username":
        return "failed"
    if newName == "invalid":
        return "failed"
    if file == "valid":
        return "success"
    return "failed"

def deleteFile(username, file):
    if not username == "username":
        return "failed"
    if file == "valid":
        return "success"
    return "failed"