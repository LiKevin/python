__author__ = 'k22li'

########################################################################################################################
# CALLABLE:  class are callable while in case the class has __call__() method being defined, would be also its instance
# callable
# question:  when to use this kind of instance calling?
########################################################################################################################

class Surprise():

    def __init__(self, num):
        self.num = num

    def __call__(self, other):
        print '>>> __call__() method is calling...'
        return self.__mod__(other)

    def __mod__(self, other):
        print '>>> __mod__() method is calling...'
        return self.num % other


########################################################################################################################
# chr & ord:  get the integer & chr values of the inputs, inputs should be in [0 ..255]
# question:  --
########################################################################################################################

# see the "Demo 2"


class ChrOrd():

    def __init__(self, input):
        self.input = input

    def __call__(self):

        if isinstance(self.input, int):
            return chr(self.input)
        elif isinstance(self.input, basestring):
            return ord(self.input)
        else:
            print '>>> Invalid input type: %s' %type(self.input)

if __name__ == '__main__':

    #################################################### Demo 1 ########################################################
#    seven  = Surprise(7)
#    print seven(4)

    #output:
    # >>> __call__() method is calling...
    # >>> __mod__() method is calling...
    # 3

    #################################################### Demo 2 ########################################################
    charod = ChrOrd()
    print charod()