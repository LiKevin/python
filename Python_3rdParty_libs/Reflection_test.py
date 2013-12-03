__author__ = 'k22li'


import sys, copy

class Animal():
    """test reflection basis"""
    def __init__(self, name):
        self.name = name

    def printName(self):
        print self.name



if __name__ == "__main__":
    """test reflection basis -- main"""
    cat = Animal('kitty')
#    print cat.name
#    cat.printName()


    if hasattr(cat, 'name'):
        print getattr(cat, 'name')
        setattr(cat,'name', 'tougher')

    cat.printName()

#
#    print dir(testInstance)
#
#    k = globals()['testInstance']
#
#    print 'reflection', k.printName()