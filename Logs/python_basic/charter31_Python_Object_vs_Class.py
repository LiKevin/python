# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpose;
# pyhton 的class 与java，c++的大不相同，经过一段时间的迷茫，总结一下：
#   1.pyhton里所有的东西都是对象，即class也是一个对象，java里的class虽然也是一个Class的实例，但基本上是一个数据和函数的集合体，
#       是不放具体东西的，但python不一样，不一样的地方如下：
#       a. python里所有对象可以动态地添加新的属性，当类动态地添加属性后，类的实例都能访问到该对象;--fixme: why dynamic languages???
#       b. 类里的变量是不是以self,开头定义的都是类变量，相当于java,c++里的static，所有实例共享他们
#       c.函数都是实现为descriptor
#       d.每个实例有__dict__用来存放动态的属性
#       e.继承：当继承后，python不会向java，c++那样在子类的实例中包含父类的实例，子类的实例是个全新的对象，与父类一点关系都没有，
#           不会包含有父类的任何东西，继承只是在子类的__base__指向了父类，在查找函数，属性的过程中会查找父类，
#           仅此而已，而这个父类也是class对象
########################################################################################################################

# demo 1: dynamic language demo
########################################################################################################################
class A(object):
    pass

def _test_dynamic_add_class_attr():
    # add class variables to Class
    A.name = 'kevin'
    # print A.__dict__ members
    print '>>> from A: %s' %A.__dict__    # {'__dict__': <attribute '__dict__' of 'A' objects>, '__module__': '__main__', \
                        # '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None, 'name': 'kevin'}

    # create instance of A()
    a = A()
    # check the default values of instance "a"
    print '>>> from a: %s' %a.__dict__  # {} nothing would be devired from base class

    # add class variables to Class dynamically, purpose is to check whether this newly updated attr would be \
    # available for "a" which is instancilized before the dync changing
    A.age = 32

    # dynamic update the attrs for the instance
    a.__dict__.update({'sex': 'Male'})

    print '>>> from a: a.sex: %s' %a.sex
    print '>>> from a: a.name: %s' %a.name # devired from the base class, but do not exist in "a.__dict__"
    print '>>> from a: a.age: %s' %a.age # devired from the base class, but do not exist in "a.__dict__"
    print '>>> from A: again check the impact from child dync update: %s' %A.__dict__   # base class's __dict__ won't \
                                                                                        # be impacted from the child's
                                                                                        # update

# outputs from "_test_dynamic_add_class_attr()"
#>>> from A: {'__dict__': <attribute '__dict__' of 'A' objects>, '__module__': '__main__', '__weakref__': \
#               <attribute '__weakref__' of 'A' objects>, '__doc__': None, 'name': 'kevin'}
#>>> from a: {}
#>>> from a: a.sex: Male
#>>> from a: a.name: kevin
#>>> from a: a.age: 32  #fixme: need to understand the class parsing progress !!! the dynamic appended variables are
                        #fixme: visible to its instance created before the changes
                        #fixme： 栈和堆的概念：instance object 按引用传递 base 类的内存地址？？？
#>>> from A: again check the impact from child dync update: {'__module__': '__main__', 'name': 'kevin', 'age': 32, \
#                                                            '__dict__': <attribute '__dict__' of 'A' objects>, \
#                                                            '__weakref__': <attribute '__weakref__' of 'A' objects>, \
#                                                            '__doc__': None}


# demo 2: check the defaults variables declared in "Class" which was inheriated from "Object"
########################################################################################################################
class B(object):
    pass

class C():
    pass

# test 2
def _test_default_attrs_inheritated_from_obj():

    obj_attrs_dict = object.__dict__    #fixme: dir(object) == print object.__dict__.keys()
    for attr_name_obj, attr_value_obj  in obj_attrs_dict.items():
        print attr_name_obj, ' %s> '%('-'*(100-len(attr_name_obj)-len(str(attr_value_obj)))), attr_value_obj

# outputs:
#    __setattr__  ----------------------------------------->  <slot wrapper '__setattr__' of 'object' objects>
#    __reduce_ex__  ------------------------------------------->  <method '__reduce_ex__' of 'object' objects>
#    __new__  ------------------------------->  <built-in method __new__ of type object at 0x000000001E2987C0>
#    __reduce__  ------------------------------------------------->  <method '__reduce__' of 'object' objects>
#    __str__  ------------------------------------------------->  <slot wrapper '__str__' of 'object' objects>
#    __format__  ------------------------------------------------->  <method '__format__' of 'object' objects>
#    __getattribute__  ------------------------------->  <slot wrapper '__getattribute__' of 'object' objects>
#    __class__  ------------------------------------------------>  <attribute '__class__' of 'object' objects>
#    __delattr__  ----------------------------------------->  <slot wrapper '__delattr__' of 'object' objects>
#    __subclasshook__  ------------------------------------->  <method '__subclasshook__' of 'object' objects>
#    __repr__  ----------------------------------------------->  <slot wrapper '__repr__' of 'object' objects>
#    __hash__  ----------------------------------------------->  <slot wrapper '__hash__' of 'object' objects>
#    __sizeof__  ------------------------------------------------->  <method '__sizeof__' of 'object' objects>
#    __doc__  --------------------------------------------------------------------------->  The most base type
#    __init__  ----------------------------------------------->  <slot wrapper '__init__' of 'object' objects>


    print '*' * 100
    obj_attrs_dict = B.__dict__
    for attr_name_B, attr_value_B  in obj_attrs_dict.items():
        print attr_name_B, ' %s> '%('-'*(100-len(attr_name_B)-len(str(attr_value_B)))), attr_value_B

# outputs:
#    __dict__  ------------------------------------------------------->  <attribute '__dict__' of 'B' objects>
#    __module__  ---------------------------------------------------------------------------------->  __main__
#    __weakref__  ------------------------------------------------->  <attribute '__weakref__' of 'B' objects>
#    __doc__  ----------------------------------------------------------------------------------------->  None

    print '*' * 100
    b = B()
#    print dir(b)    #fixme： 区分dir 和 dict 对于子类实例来说
    print b.__dict__

# outputs:
#    {}     #empty __dict__ for new instance


# test 3
def _test_dir_values_from_object_class_instance():
    '''
    check the difference among the dir() values from object/ class and its instance
    '''
    # for dir(object)
    print '*' * 100
    for item in dir(object):
        print item, ' %s> '%('-'*(100-len(item)-len(str(getattr(object, item))))), str(getattr(object, item))

# outputs:
#    __class__  ------------------------------------------------------------------------------>  <type 'type'>
#    __delattr__  ----------------------------------------->  <slot wrapper '__delattr__' of 'object' objects>
#    __doc__  --------------------------------------------------------------------------->  The most base type
#    __format__  ------------------------------------------------->  <method '__format__' of 'object' objects>
#    __getattribute__  ------------------------------->  <slot wrapper '__getattribute__' of 'object' objects>
#    __hash__  ----------------------------------------------->  <slot wrapper '__hash__' of 'object' objects>
#    __init__  ----------------------------------------------->  <slot wrapper '__init__' of 'object' objects>
#    __new__  ------------------------------->  <built-in method __new__ of type object at 0x000000001E2987C0>
#    __reduce__  ------------------------------------------------->  <method '__reduce__' of 'object' objects>
#    __reduce_ex__  ------------------------------------------->  <method '__reduce_ex__' of 'object' objects>
#    __repr__  ----------------------------------------------->  <slot wrapper '__repr__' of 'object' objects>
#    __setattr__  ----------------------------------------->  <slot wrapper '__setattr__' of 'object' objects>
#    __sizeof__  ------------------------------------------------->  <method '__sizeof__' of 'object' objects>
#    __str__  ------------------------------------------------->  <slot wrapper '__str__' of 'object' objects>
#    __subclasshook__  ------------->  <built-in method __subclasshook__ of type object at 0x000000001E2987C0>

    # for dir(class inheriated from object)
    print '*' * 100
    for item in dir(B):
        print item, ' %s> '%('-'*(100-len(item)-len(str(getattr(B, item))))), str(getattr(B, item))
# outputs:
#    __class__  ------------------------------------------------------------------------------>  <type 'type'>
#    __delattr__  ----------------------------------------->  <slot wrapper '__delattr__' of 'object' objects>
#    __dict__  >  {'__dict__': <attribute '__dict__' of 'B' objects>, '__module__': '__main__', '__weakref__': \
#                   <attribute '__weakref__' of 'B' objects>, '__doc__': None}
#    __doc__  ----------------------------------------------------------------------------------------->  None
#    __format__  ------------------------------------------------->  <method '__format__' of 'object' objects>
#    __getattribute__  ------------------------------->  <slot wrapper '__getattribute__' of 'object' objects>
#    __hash__  ----------------------------------------------->  <slot wrapper '__hash__' of 'object' objects>
#    __init__  ----------------------------------------------->  <slot wrapper '__init__' of 'object' objects>
#    __module__  ---------------------------------------------------------------------------------->  __main__
#    __new__  ------------------------------->  <built-in method __new__ of type object at 0x000000001E2987C0>
#    __reduce__  ------------------------------------------------->  <method '__reduce__' of 'object' objects>
#    __reduce_ex__  ------------------------------------------->  <method '__reduce_ex__' of 'object' objects>
#    __repr__  ----------------------------------------------->  <slot wrapper '__repr__' of 'object' objects>
#    __setattr__  ----------------------------------------->  <slot wrapper '__setattr__' of 'object' objects>
#    __sizeof__  ------------------------------------------------->  <method '__sizeof__' of 'object' objects>
#    __str__  ------------------------------------------------->  <slot wrapper '__str__' of 'object' objects>
#    __subclasshook__  ------------->  <built-in method __subclasshook__ of type object at 0x0000000002427368>
#    __weakref__  ------------------------------------------------->  <attribute '__weakref__' of 'B' objects>

    # for dir(instance of class)
    b = B()
    print '*' * 100
    for item in dir(b):
        print item, ' %s> '%('-'*(100-len(item)-len(str(getattr(b, item))))), str(getattr(b, item))

# outputs:  for b
#    __class__  ----------------------------------------------------------------------->  <class '__main__.B'>
#    __delattr__  ------------------------->  <method-wrapper '__delattr__' of B object at 0x0000000002492908>
#    __dict__  ------------------------------------------------------------------------------------------>  {}
#    __doc__  ----------------------------------------------------------------------------------------->  None
#    __format__  ---------------------------->  <built-in method __format__ of B object at 0x0000000002492908>
#    __getattribute__  --------------->  <method-wrapper '__getattribute__' of B object at 0x0000000002492908>
#    __hash__  ------------------------------->  <method-wrapper '__hash__' of B object at 0x0000000002492908>
#    __init__  ------------------------------->  <method-wrapper '__init__' of B object at 0x0000000002492908>
#    __module__  ---------------------------------------------------------------------------------->  __main__
#    __new__  ------------------------------->  <built-in method __new__ of type object at 0x000000001E2987C0>
#    __reduce__  ---------------------------->  <built-in method __reduce__ of B object at 0x0000000002492908>
#    __reduce_ex__  ---------------------->  <built-in method __reduce_ex__ of B object at 0x0000000002492908>
#    __repr__  ------------------------------->  <method-wrapper '__repr__' of B object at 0x0000000002492908>
#    __setattr__  ------------------------->  <method-wrapper '__setattr__' of B object at 0x0000000002492908>
#    __sizeof__  ---------------------------->  <built-in method __sizeof__ of B object at 0x0000000002492908>
#    __str__  --------------------------------->  <method-wrapper '__str__' of B object at 0x0000000002492908>
#    __subclasshook__  ------------->  <built-in method __subclasshook__ of type object at 0x0000000002457368>
#    __weakref__  ------------------------------------------------------------------------------------->  None

    # for dir(instance of class which was not subclass of "object")
    c = C()
    print '*' * 100
    for item in dir(c):
        print item, ' %s> '%('-'*(100-len(item)-len(str(getattr(c, item))))), str(getattr(c, item))

# outputs:
#    __doc__  ----------------------------------------------------------------------------------------->  None
#    __module__  ---------------------------------------------------------------------------------->  __main__


########################################################################################################################
# test codes
########################################################################################################################
if __name__ == '__main__':
#
#    # test demo 1
#    _test_dynamic_add_class_attr()


#    _test_default_attrs_inheritated_from_obj()

    _test_dir_values_from_object_class_instance()