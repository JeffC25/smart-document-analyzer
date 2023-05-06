import sys
sys.path.append('../')
from app.nlp import Content

sampleText = '''
David Zaslav (LAW’85), president and CEO of Warner Bros. Discovery, will deliver Boston University’s 150th Commencement address on Sunday, May 21, on Nickerson Field. 

BU President Robert A. Brown shared the news Thursday morning during the Class of 2023 Senior Breakfast at the George Sherman Union’s Metcalf Ballroom. An estimated 2,500 students were in attendance, making it the largest Senior Breakfast in history. In addition to the ballroom, students were seated in the GSU food court, which was appropriately decked out for the occasion, with white tablecloths, a jazz band, and a big-screen TV that aired the ceremony live. 

The reading of Zaslav’s name received tepid applause from students in the ballroom. But alums’ response on social media immediately after the breakfast was of disappointment—and even anger. Members of the Writers Guild of America (WGA) are currently on strike for fair pay, and as CEO of a major media conglomerate, Zaslav is one of many Hollywood executives at the center of these negotiations.

“How many of your alumni—especially my fellow COM alumni—are on the picket right now, fighting for fair wages while execs like Zaslav sit pretty?” one comment on BU’s Instagram page said. “I’m just saying, if I were graduating this year, my cap and gown would be decorated with some pro-WGA sentiments. That’d be pretty cool to see, especially from COM…” said another alum on Twitter.

Addressing the graduating seniors, Brown said that he never could have imagined that they would have had such a tumultuous college career, referencing the COVID-19 pandemic that sent them home second semester of their freshman year and then led to a “complicated” return that following fall. “Do you know how many PCR tests you had? But you made it!” Brown said. 
'''

content = Content(sampleText)
content.summarize()
content.getKeywords()
content.getPolarity()

print(content.summary)
print(content.keywords)
print(content.polarity)