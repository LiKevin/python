__author__ = 'k22li'

def modulus(x, y):
    return x % y

class Surprise():

    def __init__(self, num):
        self.num = num

    def __call__(self, *args, **kwargs):
        print "Now the instance of Surprise class is called!"

    def __mod__(self, other):
        print self.num + other
#        print self.apply("mod", self, other)

    def __gt__(self, other):
        return self.num + other

    def __pow__(self, power, modulo=None):
        self.result = 1
        for time in range(power):
            self.result *= self.num
        return self.result

if __name__ == '__main__':
    seven = Surprise(7)
    four =  Surprise(4)

    four()  # __call__ makes the INSTANCE of the calls also callable
    four % 5    # __mod__ definition working as expression of "%"
    print four > 5  # __gt__ definition working as expression of ">"
    print seven**3 # __pow__ definition working as expression of "**"
    print modulus(7, 4)