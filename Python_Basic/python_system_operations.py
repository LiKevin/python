__author__ = 'k22li'

import os

import subprocess
p = subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE, stderr = subprocess.STDOUT)

for line in p.stdout.readlines():
    print line.strip('\n\r')


#res = os.Popen('dir').readlines()
#
#for line in res:
#    print line.strip('\n\r')

def tests():
    a  = test

print globals().has_key('tests')

#print os.system('dir')


import commands

print commands.getoutput("date")