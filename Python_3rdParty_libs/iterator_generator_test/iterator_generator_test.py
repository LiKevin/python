__author__ = 'k22li'

class Node:

    def __init__(self, value):
#        method for initiate the class object
        self._value = value
        self._children = []

    def __repr__(self):
#        method for print formats definition
        return 'Node displaying({!r})'.format(self._value)

    def __iter__(self):
#        method for iterations / without this method for grammar can't work through ...
        return iter(self._children)

    def add_child(self, node):
    #        method for children appending as well
        self._children.append(node)


if __name__=='__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)

    for ch in root:
        print ch