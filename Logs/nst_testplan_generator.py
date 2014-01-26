__author__ = 'k22li'

import re
import os
import os.path as Path

PATH_TO_TEST=r'C:\Users\k22li\workspace\bsta\bsta\cases\test'
TARGET_PATH=r'/home/k22li/N/NST_Home/NSTRunner/cases/test'


def listAllFiles(path):

    if os.path.isdir(path):
        return os.listdir(path)
    else:
        return ''

def removeNonPythonScripts(fileList):

    if '__init__.py' in fileList:
        fileList.remove('__init__.py')
    return fileList

def caseFilter(fileName):

    patten_gourNo = re.compile('self._grouNO = \'(\d*)\'')
    patten_caseNo = re.compile('self._caseNO = \'(\d*)\'')

    file = Path.join(PATH_TO_TEST, fileName)
    if not Path.isfile(file):
        raise BaseException, 'Invalid file path provided!'
    else:
        with open(file, 'r+') as filer:
            for line in filer.readlines():
                if re.search(patten_gourNo, line):
                    groupNo = re.search(patten_gourNo, line).group(1)
                elif re.search(patten_caseNo, line):
                    caseNo = re.search(patten_caseNo, line).group(1)
            realPath=os.path.join(TARGET_PATH, fileName)
    return groupNo, caseNo, realPath

def composeTestPlan(caseDict, whiteList):

    template='<testcase no="%s" name="" location="%s" refPhone = ""/>'

    prefix ="""
<?xml version="1.0" encoding="utf-8"?>
<testplan assignTo="a030623e,b3b9521d,1a2215a" resultPath="/home/k22li/N/NST_Home/TestResult" syncQRDLog="true">
    <target-device hwversion="" osversion="" deviceid=""/>
    <testtask id="2" type="monkeyrunner" timeout="120">"""

    postfix = """    </testtask>
</testplan>"""
    print prefix
    for case in cases.items():
        if whiteList:
            if case[0] in whiteList:
                print '\t\t'+template %(case[0], case[1])
        else:
            print '\t\t'+template %(case[0], case[1])
    print postfix

if __name__  == '__main__':
    cases = {}
    whiteList = ['5900.315', '5104.895', '5104.894', '5104.818', '5104.817', '5104.851', '5900.210', '5104.851', \
                 '5104.116', '5104.944', '5104.945', '5104.946', '5104.947', '5104.951', '5104.826']

    files = listAllFiles(PATH_TO_TEST)

    scriptFiles = removeNonPythonScripts(files)
    for file in scriptFiles:
#        print file
        groupNo, caseNo, filePath = caseFilter(file)
        cases.update({groupNo+'.'+caseNo : filePath})

    composeTestPlan(cases, whiteList)
