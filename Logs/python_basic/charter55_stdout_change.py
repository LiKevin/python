import sys

_standardOutput = sys.stdout

sys.stdout = open("/home/lizhihui-kevin/workspace/log.txt", 'w')

print "Hello Kevin! for stdout testing purpose!"*30

sys.stdout = _standardOutput
