# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# Questions:
# search/ match/ findall from regular expression
# Fixme: key point:  search & match will stop when encountering with "\n" ; while findall() method last till end
########################################################################################################################

import re

def test_search(str_a):
    '''
    test the search methods working with \n signs
    '''
    pattern= re.compile('</?\w+>')
    if pattern.search(str_a):
        return pattern.search(str_a).group()
    else:
        return None

def test_match(str_a):
    '''
    test the match methods working with \n signs
    '''
    pattern = re.compile('</?\w*>')
    if pattern.match(str_a):
        return pattern.match(str_a).group()
    else:
        return None


def test_findall(str_a):
    '''
    test the method findall()
    '''
    pattern = re.compile('<\w*>')
    return pattern.findall(str_a)


########################################################################################################################
# test codes
########################################################################################################################

if __name__ == '__main__':
    s = '''<html>
                <head>
                    <title>
                        Title
                    </title>
                </head>
            </html>
        '''

    # demo 1
    ####################################################################################################################
    print test_search(s)
    # output:  stops when encountering the first \n
    # <html>

    # demo 2
    ####################################################################################################################
    print test_match(s)
    # output: stops when encountering the first \n
    # <html>

    # demo 3
    ####################################################################################################################
    print test_findall(s)
    # output: continue to search for all those string till EoF
    # ['<html>', '<head>', '<title>']
