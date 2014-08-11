# -*- coding: utf-8 -*-
__author__ = 'k22li'

######################################################################################################################
# function implementations
# purpose is to:
#   operator模块提供了 operator.itemgetter(),operator.attrgetter()函数，
#   在 Python 2.5以后还提供了operator.methodcaller() 函数
#######################################################################################################################
from operator import itemgetter, attrgetter

#import ope

class Student(object):

    def __init__(self, name, grade, age):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_tuples = [
    Student('frank', 'A', 34),
    Student('boush', 'A', 28),
    Student('vincent', 'B', 33),
    Student('jacky', 'B', 32),
    Student('kevin', 'C', 31)
]

print sorted(student_tuples, key = attrgetter('age'))
print sorted(student_tuples, key = attrgetter('name'))
#print sorted(student_tuples, key = itemgetter(1))
print sorted(student_tuples, key = attrgetter('age', 'name'))