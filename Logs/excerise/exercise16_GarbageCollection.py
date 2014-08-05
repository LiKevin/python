__author__ = 'k22li'

class Node:

    def __init__(self, val):
        self.value  = val

n1 = Node('abcd')
n2 = Node('efgh')

print n1.value
print n2.value

n1.prev = n2
n2.next = n1

print n1.value
print n2.value
