__author__ = 'k22li'

import os.path as path
testPath = r'C:/sp/usr/_phone'
print 'base name of the test path is: ', path.basename(testPath)

print 'dir name of the test path is: ', path.dirname(testPath)

print path.dirname(r'e:\test_data')

print path.split(testPath)
