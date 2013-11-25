__author__ = 'k22li'
import re

readTexts = ['10:3 pm']
time = re.search(r'\d{1,2}:\d{1,2} [a|p]m', str(readTexts)).group(0)

print time

