__author__ = 'k22li'


class C(object):
    money = 500

c = C()

print c.money

c.money = 100

print C.money
print c.money

C.money = 1000

print c.money