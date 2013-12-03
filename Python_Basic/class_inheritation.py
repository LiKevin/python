__author__ = 'k22li'

import os.path as path

print path.splitdrive(r'c:\abc\sde')

print path.splitext(r'c:\abc\sde')
print path.splitext(r'c:\abc\sde.asdfa')

print path.dirname(r'c:\abc\ada')

print path.exists(r'c:\abc')

print path.isabs(r'..\abc')


print path.splitext('PMCL01.jar')

print path.splitdrive(r'.\asdfas')