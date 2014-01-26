__author__ = 'k22li'

import sys
import os
from copy import deepcopy


oldModules = []
oldModules = sys.modules.values()[:]

import threading

newModules = []
newModules = sys.modules.values()[:]

def searchDiffFromTwoLists(a, b):
    for item in a:
        if not b.index(item):
            print item

if cmp(oldModules, newModules):
    searchDiffFromTwoLists(oldModules, newModules)

