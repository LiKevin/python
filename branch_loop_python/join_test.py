__author__ = 'k22li'

#for item in ['a', 'v']:
#    t = ' '.join(('a', 'v'))
#
#    print len(t), t
#
#
#print len(' ')

#tList = []
#for item in {'name' : 'VARCHAR(20)', 'feature' : 'VARCHAR(60)', 'featuregroup' : 'VARCHAR(160)', 'caseTitle' : 'VARCHAR(300)', 'executionResult' : 'VARCHAR(20)', 'execDate' : 'DATETIME'}.items():
#
#    t = ' '.join(item)
#
#    tList.append(t)
#
#print tList
#print tuple(tList)
#
#k = ', '.join(tuple(tList))
#print k


def printf(item1 = '', *args):

    for item in args:
        print item

attr = ('a', 'b', 'c')

printf(*attr, item1 = 'kkk')