__author__ = 'k22li'

a = [1, 2, 3]
b = ['a', 'b', 'c']

print a.extend(b)

print a


import os

basedir = r'c:/python27'

#dirpath, dirnames, filenames = os.walk(basedir)
#
#for item in os.walk(basedir):
#
#    print item


os.popen('dir ./')

import sys

print sys.argv[:]

for path in sys.argv:
    print os.path.basename(path)


print os.getcwd()

for dirPath, pathName, fileName in os.walk(os.getcwd()):
    print pathName, fileName