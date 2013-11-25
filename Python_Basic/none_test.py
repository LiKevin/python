__author__ = 'k22li'


#print type(None)
#
#print type('')

def testReturn(input = ''):
    if isinstance(input, str):
        return str
    else:
        return int


for input in ['a', 2]:
    print testReturn(input = input)