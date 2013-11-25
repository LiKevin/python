__author__ = 'k22li'
#purpose is to validate the length of the list when '' / None as the only list content
print '[\'\'] ---? ', len(['']) # 1, length of ['']
print '[] ---? ', len([]) # 0
print '[None] ---? ', len([None])

b = [None].pop()
#print type(None)
print b, isinstance(b, type(None))

a = [''].pop() # a = ''
print 'len(a)', len(a) # 0, len('')

assert [''], 'print failed to \'\''
assert [], 'Failed to []'