__author__ = 'k22li'


class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def __iter__(self):
        print '*'*20, 'now its the iter method being called'
        return iter(self._children)

    def add_child(self, child):
        self._children.append(child)

    def depth_first(self):
        yield self
        for c in self:
#            option 1;
#            yield from c.depth_first()

#            option 2
            for x in c.depth_first():
                yield x

if __name__=='__main__':

    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print ch