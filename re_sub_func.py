# -*- coding:utf-8 -*-
__author__ = 'k22li'

import re

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):

    #replace this for solution
    assert number in range(1000), 'Unsupported figure provided!'
    number = int(number)

    if number/100<=0: #check the digit in hundred position
        hundDigit=''
    else:
        hundDigit=FIRST_TEN[number/100]+' '+HUNDRED

    if number%100/10<=0: #如果十位数字为零
        tenDigit=''
        if (number%100)%10 !=0 and hundDigit!='':
            lastDigit=' '+FIRST_TEN[(number%100)%10]
        elif (number%100)%10 !=0 and hundDigit=='':
            lastDigit=FIRST_TEN[(number%100)%10]
        else:
            lastDigit = ''

    elif number%100/10>=2: #如果十位数字大于2
        if hundDigit != '': #如果百位为空
            tenDigit=' '+OTHER_TENS[number%100/10-2]
            if (number%100)%10 !=0:
                lastDigit=' '+FIRST_TEN[(number%100)%10]
            else:
                lastDigit=''
        else:
            tenDigit=OTHER_TENS[number%100/10-2]
            if (number%100)%10 !=0:
                lastDigit=' '+FIRST_TEN[(number%100)%10]
            else:
                lastDigit=''
    else:
        if hundDigit != '':
            tenDigit = ' '+SECOND_TEN[(number%100)%10]
            lastDigit = ''
        else:
            tenDigit = ''+SECOND_TEN[(number%100)%10]
            lastDigit = ''

    return hundDigit+tenDigit+lastDigit

#Some hints
#Don't forget strip whitespaces at the end of string


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"