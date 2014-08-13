__author__ = 'k22li'
import re

def constructTheFullString(data):
    for i in range(3):
        if len(data)<8:
            if data.index(':', 1)!= 2:
                data = '0'+ data
            elif data.index(':', 3) != 5:
                data = data[:data.index(':', 1)]+'0'+data[data.index(':', 1):]
            else:
                data = data[:data.index(':', 3)+1]+'0'+data[data.index(':', 3)+1:]
        else:
            break
    print data
    return data


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


def checkio(data):
    #replace this for solution
    data = constructTheFullString(data)
    morseList = convertToBinary2(data)
    morseCode = ' '.join(morseList)
    morseCode = re.sub('0', '.', morseCode)
    morseCode = re.sub('1', '-', morseCode)

    return morseCode

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("11:10:12") == ".- ...- : ..- .... : ..- ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    assert checkio("0:10:2") == ".. .... : ..- .... : ... ..-.", "Fifth Test"