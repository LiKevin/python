__author__ = 'k22li'
############################################################################################
# Demo1:  implementation via function decorator
def decorator_implementation_method(file_name, func):

    # prepare thing
    f = None
    try:
        # set up thing
        f = open(file_name, 'r')
        content = f.read()
        if not callable(func):
            return
        # deal with thing
        func(content)

    except IOError as e:
        print 'Error %s' %str(e)

    finally:
        if f:
            # tear things down
            f.close()

#@decorator_implementation_method
def output(content):
    print (content)


############################################################################################
# Demo 2:  implementation via Generator methods
def generator_implementation_method(file_name):
    '''
    via generator testing
    '''
    f = None
    try:
        f = open(file_name, 'r')
        thing = f.read()
        # for thing in f:
        yield thing

    except IOError as e:
        print 'Error %s' %str(e)

    finally:
        if f:
            f.close()

def test2(file_name):
    for content in generator_implementation_method(file_name):
        output(content)


############################################################################################
# Demo 3:  class solution
class class_implementation():

    def __init__(self, file_name):
        self.f = file_name

    def __enter__(self):
        try:
            self.fr = open(self.f, 'r')
            content = self.fr.read()
            return content
        except IOError as e:
            print 'Error %s' %str(e)
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fr:
            print 'type: %s, value:  %s, traceback: %s' %(str(exc_type), str(exc_val), str(exc_tb))
            self.fr.close()

def test3(file_name):
    with class_implementation(file_name) as thing:
        if thing:
            output(thing)


############################################################################################
################################## Main Function ###########################################
if __name__ == '__main__':
    file_name = r'exercise10_SQLDemo.py'
#    decorator_implementation_method(file_name, output)
#    test2(file_name)

    test3(file_name)