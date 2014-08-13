__author__ = 'k22li'

import re
import xml.etree.ElementTree as ET

def retrieveInfo(fileName):

    basicCounter = 0
    advanceCounter = 0
    mstCounter = 0

    tree = ET.parse(fileName)
    root = tree.getroot()
    for child in root:
        for subchild in child.getchildren():
            groupID = subchild.attrib['no']
            caseName = subchild.attrib['location'].replace('/home/nst/NSTRunner/cases/test/', '')

            if groupID.startswith('590'):
                basicCounter += 1
            elif groupID.startswith('510'):
                advanceCounter += 1
            else:
                mstCounter += 1

            print groupID, '\t', caseName

    return basicCounter, advanceCounter, mstCounter


def printfunc(*args):
    for item in args:
        print '*'*30, 'case amount is: %s'%(item)

if __name__=='__main__':

    basicNo, advaNo, mstNo = retrieveInfo(r'testplan_basic.xml')

#    for item in :
    printfunc(basicNo, advaNo, mstNo)