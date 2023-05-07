import sys
sys.path.append('../')
from app.nlp import Content
from app.nfi import getArticle

url = 'https://www.bu.edu/articles/2023/class-2023-senior-breakfast/'

content = Content(getArticle(url)[1])
content.summarize()
content.getKeywords()
content.getPolarity()

print(content.summary)
print(content.keywords)
print(content.polarity)