__author__ = 'k22li'


import re

a =  'asbbse'
string = 'asbbseadkfajkfjaljfa'
aPattern = re.compile(a)

if re.match(aPattern, string):
    print re.match(aPattern, string).group(0)


print re.search(aPattern, string).group(0)