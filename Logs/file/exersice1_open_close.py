__author__ = 'k22li'

import sys

csvFiler = open("../basic_orders.csv", 'r')
try:
    cLines = csvFiler.readlines()
    for cLine in cLines:
        sys.stdout.flush() #clean up the cache
        print cLine

finally:
    csvFiler.close()