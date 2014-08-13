#Your code here
#You can import some modules or create additional functions
import re

def listTransfer(arr):
    """
    function: juzhen zhuanzhi, 90 degrees every time
    """
    arr = [list(item) for item in arr]
    newList = [[r[col] for r in arr] for col in range(len(arr[0]))]
#    newList = map(list, zip(*arr))
    [item.reverse() for item in newList]
    resultList = []
    for item in newList:
        resultList.append(joinListToString(item))

#    resultList = [item.reverse() for item in resultList]
    return resultList

def joinListToString(arr):
    """
    Function:  convert each of the list contents into long string
    """
    newStr = ''
    for elem in arr:
#        print elem
        newStr = newStr + elem
    return newStr

def mapOutTheString(alist, blist):
    """
    Functions:  sort out those meaningfull characters
    """
    patten = joinListToString(alist)
    targetString = joinListToString(blist)

    patten = re.sub('X', '1', patten)
    patten = re.sub('\.', '0', patten)

#    print 'patten', '-->', patten
#    print 'targetString', '--->', targetString

    result = ''
    for k, v in zip(patten, targetString):
        matchResult = int(k) and v
        if not matchResult:
            matchResult = ''
        result = result + matchResult
    return result

def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.

    grille, template = data
#    print 'grille', '--->', grille
#    print 'temple', '--->', template

    first_four = mapOutTheString(grille, template)

    #convert the grille for the second_four strings
    grille = listTransfer(grille)
#    print grille
    second_four = mapOutTheString(grille, template)
    #convert the grille for the third_four strings
    grille = listTransfer(grille)
    third_four = mapOutTheString(grille, template)

    #convert the grille for the forth_four strings
    grille = listTransfer(grille)
    forth_four = mapOutTheString(grille, template)
    #replace this for solution
    return first_four+second_four+third_four+forth_four

#Some hints
#Just loop for iterations
#Maybe you will convert grille for more comfortable view


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([ \
        ['X...', \
         '..X.', \
         'X..X', \
         '....'], \
        ['itdf', \
         'gdce', \
         'aton', \
         'qrdi']]) == 'icantforgetiddqd', 'First example'

    assert checkio([ \
        ['....', \
         'X..X', \
         '.X..', \
         '...X'], \
        ['xhwc', \
         'rsqx', \
         'xqzz', \
         'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second example'
