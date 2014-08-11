__author__ = 'k22li'

#######################################################################################################################
# function implementations
# purpose is to:
#   without deleting "c", this c will stay as the value "0" for a longer period untill the GC handled by python framework
#######################################################################################################################

_alphanum = {}
for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890':
    _alphanum[c] = 1

del c

print _alphanum
