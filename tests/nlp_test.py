import sys
sys.path.append('../')
from app.nlp import Content

sampleText = "Scientists have made an exciting discovery in the field of renewable energy. They have developed a new type of solar panel that is more efficient and less expensive than existing models. The breakthrough was made possible by the use of a material called perovskite, which is cheaper and easier to produce than the materials traditionally used in solar panels. Perovskite is also able to be processed at a lower temperature, which reduces both energy consumption and production costs. The new solar panels have a higher power conversion efficiency compared to previous perovskite-based designs, meaning they can produce more electricity from the same amount of sunlight. This development has the potential to revolutionize the use of solar power as a clean and sustainable source of energy."

def test():
    content = Content(sampleText)
    content.summarize()
    content.getKeywords()
    content.getPolarity()

    print(content.summary)
    print(content.keywords)
    print(content.polarity)

test()