#-*-coding: utf-8 -*-
__author__ = 'k22li'

import re

t = [u'\u0985\u09b8\u09ae\u09c0\u09af\u09bc\u09be ', u'\u09ac\u0982\u09b2\u09be ', 'English phone keypad', u'\u0a97\u0ac1\u0a9c\u0ab0\u0abe\u0aa4\u0ac0 ', u'\u0939\u093f\u0928\u094d\u0926\u0940 ', u'\u0c95\u0ca8\u0ccd\u0ca8\u0ca1 ', u'\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02 ', u'\u092e\u0930\u093e\u0920\u0940 ', u'\u0b13\u0b5d\u0b3f\u0b06 ', u'\u0a2a\u0a70\u0a1c\u0a3e\u0a2c\u0a40 ', u'\u0ba4\u0bae\u0bbf\u0bb4\u0bcd ', u'\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41 ', u'\u0627\u0631\u062f\u0648 full keyboard', u'\u0627\u0631\u062f\u0648 phone keypad']



def _findOutTheInputLanguage(inputKeyboards = ''):
    """
    العربية full keyboard/ العربية phone keypad
    to fix this kind of issues.
    """
    fullAfterPatten = re.compile(r'(.*) full keyboard')
    fullBeforePatten = re.compile(r'full keyboard (.*)')
    phoneAfterPatten = re.compile(r'(.*) phone keypad')
    phoneBeforePatten = re.compile(r'phone keypad (.*)')

    for item in t:
        for patten in [fullAfterPatten, fullBeforePatten, phoneAfterPatten, phoneBeforePatten]:

            if patten.match(item):
                inputLanguage = patten.search(item).group(1)
                inputkeypad = patten.search(item).group(0)
                return inputLanguage, inputkeypad

    return None


l, k = _findOutTheInputLanguage(t)

print l, k