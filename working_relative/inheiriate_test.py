__author__ = 'k22li'


class pets(object):

    def naming(self, successor):
        self.successor = successor

    def voice(self):
        print 'woaf!'


class cat(pets):

    def name(self):
        print 'name is Cat!'
#        self.naming('test')
        self.successor.name()
        self.successor.name()


if __name__ == '__main__':

    testAnimal = cat()

    testAnimal.voice()
    testAnimal.name()