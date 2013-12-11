__author__ = 'k22li'

import fnmatch

name = ['dlsf', 'ewro.txt', 'te.py', 'youe.py']

#unix style regular express used as pattern reference...
print fnmatch.filter(name, '[de]*')

print fnmatch.filter(name, '[de]')

#return True/False from fnmatchcase...first params should be string or buffer format/ then followed by the patterns
print fnmatch.fnmatchcase(str(name), '[de]*')

#convert the unix formatted regular express to the normal regular express
print fnmatch.translate('[de]$')