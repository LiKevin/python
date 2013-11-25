__author__ = 'k22li'

# Error, script language, is not allowed to call the methods before defining
testMethodCalling(input=3)

#definition of the call methods
def testMethodCalling(input = ''):

    print type(input), input*2

# work scenarios, script language, is not allowed to call the methods before defining
testMethodCalling(input=3)

