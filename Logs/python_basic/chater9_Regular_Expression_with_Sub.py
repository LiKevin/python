# -*- coding: utf-8 -*-
__author__ = 'k22li'
#######################################################################################################################
# function implementations
# purpose is to:
#   搞清楚贪心匹配与非贪心匹配之间的关系/ 正则表达式，子串代替问题
#######################################################################################################################

import re

p = re.compile('(red|blue|green)')

print p.sub('colout', 'blue socket and red shoes')

print p.sub('colout', 'blue socket and red shoes', count=1)

print p.search('blue socket and red shoes').group()

print p.split('blue socket and red shoes', 3)   # split the string according to the regular \
                                                # expressions, maximum splits allowed
