__author__ = 'k22li'

class VariableValueExchange():
    """ exchange the values of two variables"""

    def __init__(self, param1, param2):
        """
         initialize the variables
        """
        self.param1 = param1
        self.param2 = param2

    def exchangeValues(self):
        """
        exchange the values of params
        """
        self.param2, self.param1 =  self.param1, self.param2
        return self.param1, self.param2

    def helper(self):
        """
         debugging the helper of functions & classes defined in the class
        """
        print '*'*78
        return help(VariableValueExchange)


if __name__ == '__main__':

    a = 1
    b = 2

    VEX = VariableValueExchange(a, b)

    c, d = VEX.exchangeValues()
    print c, d
    VEX.helper()

