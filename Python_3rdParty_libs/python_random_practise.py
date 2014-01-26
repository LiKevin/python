__author__ = 'k22li'

import random
import string

# list the functions/ attributes of random class
for command in dir(random):
    print command

# list the functions/ attributes of String class
for item in dir(string):
    print item

# test random choice
print random.choice(string.letters)

# test random sample
for i in range(10):
    print random.sample(string.letters,5)

# list all lower case letters
print string.lowercase


#print map(lambda x : ''.join(x), random.sample(string.uppercase, 2))

# join the elements from per list
print ''.join(random.sample(string.uppercase, 2))