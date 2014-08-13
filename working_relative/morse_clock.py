# -*- coding: utf8 -*-
__author__ = 'k22li'

"""
example
Help Stephen automate his task by creating a module. As you can see in the illustration, gray circles indicate a binary on while white circle indicate a binary off. Each digit in the current time string, contains the information from a different slot. The first digit for hour has a length of two, the second digit for hour has a length of four. The first digits for both the minute and second both have a length of three while the second digits for minute and second have a length of four. Each digit in the time string is converted to binary representation. For this task, you will converted every on ( or 1 ) signal to a dash ( - ) and every off ( or 0 ) signal to a dot ( . )
Input: A time string ( could be hh:mm:ss or h:m:s format depends on digit length )
Output: A string of Morse symbol from binary representation with specific format:
"h h : m m : s s"
where each digits represented as sequence of "." and "-"
"""



#number = int(input('输入十进制'))
#print number>>1
#n=''.join([str((number>>a&0x1))for a in range(3,-1,-1)]);
#print n

#for k, v in enumerate('abd'):
#    print k, v

import re

def convertToBinary(aStr):
    morseList = []
    for k, v in enumerate(aStr):
        if v != ':':
            if k == 0:
                morseCode = ''.join([str(int(v)>>a&0x1) for a in range(1, -1, -1)])
            elif k == 3 or k == 6:
                morseCode = ''.join([str(int(v)>>a&0x1) for a in range(2, -1, -1)])
            else:
                morseCode = ''.join([str(int(v)>>a&0x1) for a in range(3, -1, -1)])
        else:
            morseCode = ':'
        morseList.append(morseCode)

    return morseList

def convertToBinary2(aStr):
    morseList = []
    for k, v in enumerate(aStr):
        if v != ':':
            morseCode = ''.join([str(int(v)>>a&0x1) for a in range(3, -1, -1)])
            if k == 0:
                morseCode = morseCode[-2:]
            elif k == 3 or k == 6:
                morseCode = morseCode[-3:]
            else:
                morseCode = morseCode
        else:
            morseCode = ':'
        morseList.append(morseCode)

    return morseList
'

def checkio(data):
    #replace this for solution
    morseList = convertToBinary2(data)
    morseCode = ' '.join(morseList)
    morseCode = re.sub('0', '.', morseCode)
    morseCode = re.sub('1', '-', morseCode)
#    print morseCode
    return morseCode

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("11:10:12") == ".- ...- : ..- .... : ..- ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    assert checkio("00:10:02") == ".. .... : ..- .... : ... ..-.", 'fifth test'
