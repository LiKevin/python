__author__ = 'k22li'

"""
Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:
I, II, III, IV, V, VI, VII, VIII, IX, and X.
The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are based on combinations of these seven symbols:
Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)
More additional information about roman numerals can be found on the Wikipedia article.
For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
Input: An integer ranging from 1 to 3999.
Output: A string in the form of a Roman numeral.
"""

def checkString(number):

    #check the thousand digit
    if number/1000 >0: #check the thousand digit
        thouDigit = number/1000
        thouStr = 'M'*thouDigit
    else:
        thouStr = ''

    #check the hundred digit
    if number%1000/100>0:
        hunDigit = number%1000/100
        if hunDigit == 9:
            hunStr = 'CM'
        elif hunDigit>=5:
            hunStr = 'D'+'C'*(hunDigit-5)
        elif hunDigit == 4:
            hunStr = 'CD'
        else:
            hunStr = 'C'*hunDigit
    else:
        hunStr = ''

    #check the ten digit
    if number%1000%100>0:
        tenDigit = number%1000%100/10
        if tenDigit == 9:
            tenStr = 'XC'
        elif tenDigit >=5:
            tenStr = 'L'+'X'*(tenDigit-5)
        elif tenDigit == 4:
            tenStr = 'XL'
        else:
            tenStr = 'X'*tenDigit
    else:
        tenStr = ''

    #check the last digit
    lastDigit = number%1000%100%10
    if lastDigit == 9:
        lastStr = 'IX'
    elif lastDigit >= 5:
        lastStr = 'V' + 'I'*(lastDigit - 5)
    elif lastDigit == 4:
        lastStr = 'IV'
    else:
        lastStr = 'I'*lastDigit

    return thouStr+hunStr+tenStr+lastStr



def checkio(data):


    translateStr = checkString(data)

    #replace this for solution
    return translateStr

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'