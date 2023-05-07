from newspaper import Article

def getArticle(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return 0, article.text
    except Exception as e:
        print(e)
        return -1, None

