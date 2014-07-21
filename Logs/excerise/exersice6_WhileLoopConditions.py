__author__ = 'k22li'

"""
difference existing between python2.7 & python3.0; key is whether True keywords is a built-in variable or Global variable
"""

def w():
    while 1:
        pass

def w2():
    while True:
        pass


import dis
"""
dis module is used to re-compile the functions designed
"""
dis.dis(w)

print '*'*80

dis.dis(w2)