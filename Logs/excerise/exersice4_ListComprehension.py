__author__ = 'k22li'

class SpecificNumberSelector():
    """
    figure out the specific type of digits:  Odd / Even and print them to sys.stdout
    """

    def getEvenDigits(self, upperLimit=10):
        """
        return the list of the EVEN digits till this upper limit
        """
        return [ x for x in xrange(upperLimit) if x%2 == 0 ]     #list comprehension

    def getOddDigits(self, upperLimit=10):
        """
        return the list of the ODD digits till this upper limit
        """
        return [ x for x in xrange(upperLimit) if x%2 != 0 ]     #list comprehension

    def printing(self, *args):
        """
        do print formatting and print the indicators associated
        """
        for context in args:
            indicator = ' the %d time ' %(args.index(context))
#            format outputs, pay attention that there is not arg key-words allowed for center() method
#            !!! BAD EXAMPLE:
#            print str(indicator).center(width=40, fillchar='*')
            print str(indicator).center(40, '*')
            print context, '\n'

    def helper(self):
        """
        helper function
        """
        print '*'*40
        help(self)

if __name__ =='__main__':

    SNS = SpecificNumberSelector()

    SNS.printing(SNS.getEvenDigits(20), SNS.getOddDigits(20))

    SNS.helper()
