__author__ = 'k22li'

counter = 12


# without "break" session, then both the branches would be covered, else would just goes into one of the branches insteadly
while counter <= 10:
    print 'In scope counter!'
    counter += 1
    if counter >= 7:
        break

else:
    print 'not in scope!'