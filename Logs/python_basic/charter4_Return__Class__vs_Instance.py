__author__ = 'k22li'


class A(object):

#    @classmethod
    @staticmethod
    def new_instance(self):
        return self.__class__()



if __name__ == '__main__':

    a = A()

    a_inner = A.new_instance(a)


    print id(a_inner), type(a_inner)

    print id(a), type(a)

    print isinstance(a, A)
    print isinstance(a_inner, A)