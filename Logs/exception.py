__author__ = 'k22li'
import traceback

try:
    #1/0
    t = t+1

except Exception, e:
    print '*', e
    print "*", traceback.format_exc()