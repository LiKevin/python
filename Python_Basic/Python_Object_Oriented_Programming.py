# -*- coding: utf-8 -*-
#__author__ = 'k22li'

class exampleClass():
    eyes = 'blue'
    age = 22
    def thisMethod(self):
        print 'hey, this method working!'

print 'class itself ----> ', id(exampleClass)

exampleObject = exampleClass()

print exampleObject

print exampleObject.age

#多态形式的表征
exampleObject.age = 30
print exampleObject.age

example2Object = exampleClass()
print example2Object.age

example2Object.surname = 'Li'
print example2Object.surname

print exampleObject.surname
