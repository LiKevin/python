__author__ = 'k22li'


def test():
    if not globals().has_key('TEST'):
        global TEST
    else:
        TEST = 'ABC'


test()

TEST = 'abc'

print TEST

