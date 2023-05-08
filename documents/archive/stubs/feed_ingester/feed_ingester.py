def scrapeArticle(file, fileType):
    if file == "valid" and fileType == "valid":
        return "success"
    return "failed"

def scraperInterface(file):
    if file == "valid":
        return "success"
    return "failed"

def sentimentAnalzye(keyWords):
    if keyWords == "valid":
        return "success"
    return "failed"