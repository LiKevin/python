__author__ = 'k22li'

########################################################################################################################
# classmethod & staticmethod:  get the integer & chr values of the inputs, inputs should be in [0 ..255]
# question:  --
########################################################################################################################

class Foo():

    def test(self):
        print('>>> object methods, normal methods defined for a class/ instance method ...')

    @classmethod
    def test_class_method(cls):
        print('>>> class methods ...')

    @staticmethod
    def test_static_method():
        print('>>> static methods ...')

class Foo_Child(Foo):
    pass
    @classmethod
    def test_class_method(cls):
        print('>>> new class method defined from the child class...')

    @staticmethod
    def test_static_method():
        print('>>> new static method defined from the child class...')

if __name__ == '__main__':

    foo = Foo()
    # demo 1
    try:
        Foo.test()  # try to call the unbounded methods from the class
    except  Exception as error:
        print('>>> error, reason:  %s' %error)

    # demo 2
    foo.test() # calling the normal methods defined in the class

    # demo 3
    Foo.test_class_method()  # calling the class methods through class

    # demo 4
    foo.test_class_method() # calling the class methods through instance

    # demo 5
    Foo.test_static_method()    # calling the static methods through class

    # demo 6
    foo.test_static_method()    # calling the static methods through instance

    # demo 7
    foo_instance = Foo()
    Foo.test(foo_instance)      # workable, with the instance being passed by as param

    ###################################################################################################################
    # till now we haven't find the gaps between @classmethod & @staticmethod;
    # now let's see the how the overwritten from the sub-class works
    ###################################################################################################################

    foo_child = Foo_Child()

    # demo 9
    Foo_Child.test_class_method()

    # demo 10
    foo_child.test_class_method()

    # demo 11
    Foo_Child.test_static_method()

    # demo 12
    foo_child.test_static_method()
    ###################################################################################################################
    # still, we haven't find the gaps between @classmethod & @staticmethod;
    # because both the @classmethod & @staticmethod could be overwritten or devired from the parents
    ###################################################################################################################