__author__ = 'k22li'

def yieldTest(length = 0):

    for i in range(length):
        yield i * 3


if __name__ == '__main__':
    n = 10
    k = yieldTest(n)

    print k

    for i in range(n+1):

        try:
            print k.next()
        except StopIteration as e:
            print 'failed to iterating, reason: %s' %e