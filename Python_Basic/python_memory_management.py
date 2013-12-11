__author__ = 'k22li'
;
import gc
import objgraph

print map((lambda x : x), dir(objgraph))