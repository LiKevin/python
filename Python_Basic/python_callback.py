__author__ = 'k22li'


class test:

    def my_callback(self, input):
        print "function my_callback was called with %s input" % (input,)

    def caller(self, input, func):
        func(input)


    def test(self):
        self.caller(5, self.my_callback)


if __name__ == '__main__':

    t = test()

#    for i in range(5):
#        t.caller(i, t.my_callback)
    t.caller()

import atexit as ae
print dir(ae)
