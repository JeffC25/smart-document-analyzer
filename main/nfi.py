# from nltk.corpus import stopwords
# from nltk.tokenize import sent_tokenize
# import nltk.downloader
# from textblob import TextBlob
from newspaper import Article
import requests
from bs4 import BeautifulSoup

def getArticle(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return article.text, 0
    except Exception as e:
        print(e)
        return None, -1

print(getArticle('https://www.bu.edu/articles/2023/class-2023-senior-breakfast/')[0])

