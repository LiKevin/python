__author__ = 'k22li'

my_list = ['a', 'b', 'c', 'd']

# by default the start counting index number is 0
print 'here is the demonstration of the index calculation starting from 0'
for idx, val in enumerate(my_list):
    print (idx, val)


# setting the start index number as param of enumerate() method
print 'by given the start point from 1'
for idx, val in enumerate(my_list, 1):
    print (idx, val)