__author__ = 'k22li'

condList = ['a', 'b', 'c']

for k in condList:
    if k == 'a':
        print 'Matched content detected!'
        break

else:
    print 'None of the matches founded!'

print 'Already outside of the loops!'