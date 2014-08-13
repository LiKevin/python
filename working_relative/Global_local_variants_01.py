__author__ = 'k22li'


#example
counter = 1
def foo():
    m = 3

    def bar():
        global counter
        counter += 1
        n = 4
        print counter, m+n
        print bar()
    bar()

foo()