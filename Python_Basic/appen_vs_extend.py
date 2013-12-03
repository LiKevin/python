__author__ = 'k22li'
"""
difference between extend & append
"""

a = list(('a', 'b', 'c'))

print a

a.append('d')

print a

a.extend('f')

print a

a.append(['h'])

print a

a.extend(['i', 'j'])

print a