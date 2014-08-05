# -*- coding: utf-8 -*-
__author__ = 'k22li'
__doc__ = '''
字符串S反转之后还是字符S，我们就称字符串S为回文。例如：字符串 "abcba" 就是回文，字符串"abc"不是回文
现要求设计一个函数，输入一个字符串，如果该字符串在重排字符顺序之后，有可能成为一个回文，该函数就返回1，否则返回0
例如： 字符串"ccbba"，将其重排成"cbabc"之后，变成了一个回文，因此函数返回1
字符串"ccba"，无论怎样重排，都不是成为一个回文，因此函数返回0
'''
import sets

def string_reverse_check(a_string):

    i = 0
    unique_elem = list(sets.Set(a_string))

    for item in unique_elem:
        if bool(a_string.count(item) % 2):
            i += 1

    if i<=1:
        return 1
    else:
        return 0


if __name__ == '__main__':

    string_a = 'abcddcbawer'

    print string_reverse_check(string_a)

