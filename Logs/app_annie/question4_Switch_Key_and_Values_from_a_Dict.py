__author__ = 'k22li'


aList = ['a', 'b', 'c', 'd']
aDict = dict(enumerate(aList))

def switch_key_values_from_a_dict(aDict):
    if not aDict:
        return {}
    else:
        return dict(zip(aDict.values(), aDict.keys()))

def output(content):

    print 'Content are: %s' %(content)

if __name__ == '__main__':

    output(aDict)
    output(switch_key_values_from_a_dict(aDict))