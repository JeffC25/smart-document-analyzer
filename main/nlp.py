import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from textblob import TextBlob
from heapq import nlargest
import string
import yake

class Content:
    def __init__(self, text):
        nltk.download("stopwords", quiet=True)
        self.text = text
        self.summary = None
        self.keywords = set()
        self.sentiment = 0

    def summarize(self, weight=0.3):
        textContent = self.text
        try:
            stopWords = stopwords.words('english')
            punctuation = string.punctuation + '“' + '”' + '…' + '’' + '' '\n'

            wordFrequencies = dict()
            for word in nltk.word_tokenize(textContent.lower()):
                if word not in stopWords and word not in punctuation:
                    if word not in wordFrequencies:
                        wordFrequencies[word] = 1
                    else:
                        wordFrequencies[word] += 1

            maxFrequency = max(wordFrequencies.values())
            for word in wordFrequencies.keys():
                wordFrequencies[word] = (wordFrequencies[word]/maxFrequency)

            sentenceWeight = dict()
            for sentence in nltk.sent_tokenize(textContent):
                # word count in current sentece
                wordCount = len(nltk.word_tokenize(sentence))
                
                # word count without stop words
                withoutStopwords = 0

                for wordWeight in wordFrequencies:
                    if wordWeight in sentence.lower():
                        withoutStopwords += 1
                        
                        if sentence in sentenceWeight:
                            sentenceWeight[sentence] += wordFrequencies[wordWeight]
                        else:
                            sentenceWeight[sentence] = wordFrequencies[wordWeight]
                
                sentenceWeight[sentence] = sentenceWeight[sentence]

            selectLength = int(len(sentenceWeight) * weight)
            summarySentences = [word for word in nlargest(selectLength, sentenceWeight, key = sentenceWeight.get)]
            summary = ' '.join(summarySentences)

            self.summary = summary
            return 0, summary    
        
        except Exception as e:
            print(e)
            return -1, None
        

    def getKeywords(self):
        textContent = self.text
        try:
            extractor = yake.KeywordExtractor(top=10, stopwords=stopwords.words('english'))
            keywords = extractor.extract_keywords(textContent)
            keywordSet = set()
            for i in keywords:
                keywordSet.add(i[0])

            self.keywords = keywordSet
            return 0, keywordSet
        except Exception as e:
            print(e)
            return -1, None

    def summarize(self):
        textContent = self.text
        try:
            analysis = TextBlob(textContent)
            self.sentiment = analysis.polarity
        except Exception as e:
            print(e)
            return -1, None