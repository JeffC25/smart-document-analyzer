# from nltk.corpus import stopwords
# from nltk.tokenize import sent_tokenize
# import nltk.downloader
# from textblob import TextBlob
from newspaper import Article
# import requests
# from bs4 import BeautifulSoup

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

