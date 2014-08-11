# -*- coding: utf-8 -*-
__author__ = 'k22li'

#######################################################################################################################
# function implementations
# purpose is to:
#   查找一个age最高的name
#######################################################################################################################

def get_the_yongest_name_return_tuple(person_dict):

    '''
    sort the names by his/her age, return the yongest one's info in tuple
    '''
    name_sorted = sorted(person_dict.items(), key=lambda x: x[1])
    name = name_sorted.pop(0)
    del name_sorted #clean up the memory once the list isnt useful
    return name

def get_the_yongest_name_return_string(person_dict):
    '''
    sort the names by his/her age, return the yongest ones' name
    '''
    name_sorted =  sorted(person_dict, key=lambda x : person_dict[x])
    name = name_sorted.pop(0)
    del name_sorted
    return name

#######################################################################################################################
# function implementations
# purpose is to:
#   通常情况下，对于复杂结构进行排序，通常使用索引作为比较的key
#######################################################################################################################
#demo 1

student_tuples = [
    ('frank', 'A', 34),
    ('boush', 'A', 28),
    ('vincent', 'B', 33),
    ('jacky', 'B', 32),
    ('kevin', 'C', 31)
]

print sorted(student_tuples, key=lambda x : x[2])
del student_tuples


#demo 2
class Student():

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

print sorted(student_tuples, key=lambda student : student.age)
del student_tuples

#######################################################################################################################
# test codes
#######################################################################################################################


if __name__ == '__main__':

    person = {'shao':23, 'wang':20, 'zhang':21, 'he':22}

    print get_the_yongest_name_return_tuple(person)
    print person.items()

    print get_the_yongest_name_return_string(person)