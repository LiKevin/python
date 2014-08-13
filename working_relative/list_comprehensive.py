# -*- coding:utf-8 -*-
__author__ = 'k22li'

smile_icons_verify = [':,(', ':@', ':)', ':$', ':(', ':P', ':O', ':*', ':))', ':B', ':D', ':-/', ':S', ':|']

smile_icons_all = [':,(', 'ad', 'cd', ':@', ':)', ':$', ':(', ':P', ':O', ':*', ':))', ':B', ':D', ':-/', ':S', ':|']

smile_icons_input = [item for item in smile_icons_all if item.startswith(':')]
"""
列表解析：分支语句需在后面
"""
print 'abc'.startswith('a')

print smile_icons_input