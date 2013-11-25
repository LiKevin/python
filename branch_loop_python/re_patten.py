# -*- coding:  utf-8 -*-
__author__ = 'k22li'
import re


def _findOutTheInputLanguage(inputKeyboards = ''):
    """
    العربية full keyboard/ العربية phone keypad
    to fix this kind of issues.
    """
    fullAfterPatten = re.compile(r'(.*) full keyboard')
    fullBeforePatten = re.compile(r'full keyboard (.*)')
    phoneAfterPatten = re.compile(r'(.*) phone keypad')
    phoneBeforePatten = re.compile(r'phone keypad (.*)')

    for patten in [fullAfterPatten, fullBeforePatten, phoneAfterPatten, phoneBeforePatten]:

        if patten.match(inputKeyboards):
            inputLanguage = patten.search(inputKeyboards).group(1)
            return inputLanguage

    return None


t = _findOutTheInputLanguage(inputKeyboards = 'العربية phone keypad')
print t
