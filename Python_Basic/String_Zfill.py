__author__ = 'k22li'

"""Pad a numeric string on the left with zero digits until the given width is reached. Strings starting with a sign are handled correctly"""

strLetter = 'abc'

print strLetter.zfill(6)
# return would be '000abc'