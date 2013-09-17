__author__ = 'k22li'
#
#aStr = '1000001010010000'
#bStr = 'itdfgdceatonqrdi'
#
#for k, v in zip(aStr, bStr):
#    print k, v
#
#a, b = [['ac', 'ef'], ['bd', 'hg']]
#
#print a, '\n', b
#
#
#for item in a:
#    print item

#theList = ['X...', '..X.', 'X..X', '....']
#
#def joinListToString(arr):
#    """
#    Function:  convert each of the list contents into long string
#    """
#    newStr = ''
#    for elem in arr:
##        print elem
#        newStr = newStr + elem
#        newStr = newStr + elem
#    return newStr
#
#
#t = joinListToString(theList)
#
#print t
#
#alist = [['a'],['b'],['c'],['d']]
#
#print [ele for ele in [item.pop() for item in alist]]
#
#print list('abcd')
arr = ['X...',\
       '..X.',\
       'X..X',\
       '....']

arr = [list(item) for item in arr]

new_arr = [[r[col] for r in arr] for col in range(len(arr[0]))]
print new_arr
[item.reverse() for item in new_arr]
print new_arr
