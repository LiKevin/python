__author__ = 'k22li'


import random
import string


for i in range(10):
    print ''.join(random.sample(string.digits, 9))