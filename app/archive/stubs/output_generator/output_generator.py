def downloadFile(username, file):
    if not username == "valid":
        return "failed"
    if file == "valid":
        return "success"
    return "failed"

def downloadFolder(username, folder):
    if not username == "valid":
        return "failed"
    if folder == "valid":
        return "success"
    return "failed"