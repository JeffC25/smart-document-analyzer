import sys
sys.path.append('../')
from app.nlp import Content
from app.sfu import uploadFile

def test():
    content = Content(uploadFile('sample_pdf.pdf')[1])
    content.summarize()
    content.getKeywords()
    content.getPolarity()

    print(f'Summary: {content.summary}')
    print(f'Keywords: {content.keywords}')
    print(f'Polarity: {content.polarity}')

test()