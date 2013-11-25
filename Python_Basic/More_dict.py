__author__ = 'k22li'


ages = {'dad' :  42, 'mom' : 48, 'lisa':7}

for item in ages:
    print item


for item in ages:
    print item, ages[item]


for k, v in ages.items():
    print k, v