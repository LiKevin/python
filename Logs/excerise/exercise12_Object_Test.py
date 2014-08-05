__author__ = 'k22li'


class ClassDemo(object):
    '''
    testing the object reflection methods
    '''

    def __init__(self):

        print hasattr(self, "__class__")
        print hasattr(self, "__name__")
        print hasattr(self, '__author__')
        print hasattr(self, '__doc__')
        print hasattr(self, '__repr__')



if __name__ == '__main__':

    CD = ClassDemo()

