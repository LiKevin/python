__author__ = 'k22li'
import re

allTexts = ['01:23', '20:00', '120:00']

patten = re.compile('\d\d:\d\d')
for text in allTexts:
    if re.match(patten, text):
        print text
        break