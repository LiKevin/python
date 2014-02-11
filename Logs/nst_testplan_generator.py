__author__ = 'k22li'

import re
import os
import os.path as Path

#   path to all those available test scripts
PATH_TO_TEST=r'C:\Users\k22li\workspace\bsta\bsta\cases\test'
#   path to the test environment where to fetch those test scripts for executions
#TARGET_PATH=r'/home/k22li/N/NST_Home/NSTRunner/cases/test'
TARGET_PATH=r'/home/nst/NSTRunner/cases/test'
#   path to NST test result storage
#RES_PATH=r'/home/k22li/N/NST_Home/TestResult'
RES_PATH=r'/home/nst/TestResult'
#   execution duration for nst runs
EXEC_DURATION='120'
BASIC_EXEC_DURATION='40'
ADVANCED_EXEC_DURATION='80'

#######################################################################################################################
#Sub-Functions
#######################################################################################################################
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
    patten_refPhone = re.compile('self.refPhone|RefHelpers')
    file = Path.join(PATH_TO_TEST, fileName)
    if not Path.isfile(file):
        raise BaseException, 'Invalid file path provided!'
    else:
        with open(file, 'r+') as filer:
            refPhone = 'False'
            for line in filer.readlines():
                if re.search(patten_gourNo, line):
                    groupNo = re.search(patten_gourNo, line).group(1)
                elif re.search(patten_caseNo, line):
                    caseNo = re.search(patten_caseNo, line).group(1)
                elif re.search(patten_refPhone, line):
                    refPhone='True'
#            realPath=os.path.join(TARGET_PATH, fileName)
            realPath=TARGET_PATH+'/'+fileName
    return groupNo, caseNo, realPath, refPhone

def composeTestPlan(deviceIDs, caseList, whiteList, debug):

    template='<testcase no="%s" name="" location="%s" refPhone = "%s"/>'

    prefix ="""<?xml version="1.0" encoding="utf-8"?>\n<testplan assignTo="%s" resultPath="%s" syncQRDLog="true">\n\t<target-device hwversion="" osversion="" deviceid=""/>\n\t<testtask id="1" type="monkeyrunner" timeout="%s">"""

    taskTemplate='\t<testtask id="2" type="monkeyrunner" timeout="%s">'

    taskending='\t</testtask>'

    postfix = """\t</testtask>\n</testplan>"""

    counter = 0
    isFirstAdvancedCase = True

#   take 5900 as basic group number; while 5104 as advanced number
    caseList.sort(reverse=True)


    if debug:
        print prefix %(deviceIDs, RES_PATH, BASIC_EXEC_DURATION)
        for case in caseList:
            if whiteList:
                if case[0] in whiteList:
#                    add the 2nd task bulletin for advanced cases
                    if case[0].startswith('51') and isFirstAdvancedCase:
                        print taskTemplate %(ADVANCED_EXEC_DURATION)
                        isFirstAdvancedCase = False
                    print '\t\t'+template %(case[0], case[1], case[2])
                    counter += 1
            else:

#               add the 2nd task bulletin for advanced cases
                if case[0].startswith('51') and isFirstAdvancedCase:
                    print taskTemplate %(ADVANCED_EXEC_DURATION)
                    isFirstAdvancedCase = False
                print '\t\t'+template %(case[0], case[1], case[2])
                counter += 1
        print postfix
    else:
        with open('testplan.xml', 'w+') as filer:
            filer.write(prefix %(deviceIDs, RES_PATH, BASIC_EXEC_DURATION))
            filer.write('\n')
            for case in caseList:
                if whiteList:
                    if case[0] in whiteList:
#                       add the 2nd task bulletin for advanced cases
                        if case[0].startswith('51') and isFirstAdvancedCase:
                            filer.write(taskTemplate %ADVANCED_EXEC_DURATION)
                            filer.write('\n')
                            isFirstAdvancedCase = False
                        filer.write('\t\t'+template %(case[0], case[1], case[2]))
                        filer.write('\n')
                        counter += 1
                else:
#                   add the 2nd task bulletin for advanced cases
                    if case[0].startswith('51') and isFirstAdvancedCase:
                        filer.write(taskending)
                        filer.write('\n')
                        filer.write(taskTemplate %ADVANCED_EXEC_DURATION)
                        filer.write('\n')
                        isFirstAdvancedCase = False
                    filer.write('\t\t'+template %(case[0], case[1], case[2]))
                    filer.write('\n')
                    counter += 1
            filer.write(postfix)

    print '\n'+'*'*30+str(counter)+'*'*30

def whiteListProcessor(rawList):

    if  len(rawList):
        if rawList.startswith('['):
            whiteList = eval(rawList)
        else:
            whiteList = re.split(r'[\[,;\s\n\]]\s*', rawList)
    else:
        print 'Kindly check the "RawList" provided, which might not in good format: %s' %rawList

    return whiteList

def debuggingLines():

    print '\n'+'*'*120+'\n'


#######################################################################################################################
#Main-Functions
#######################################################################################################################
if __name__  == '__main__':

    cases = []
    N1DeviceGroup = 'a030623e,b3b9521d,1a2215a'
    N2DeviceGroup = '995b62e7,995b62f9,995b6330,995b63d2,99626218'

    productSelection = raw_input( \
        'Would you like to create testplan.xml for N1 or N2?\nYour selection (n1 | n2): ')

    if productSelection in ['N1', 'n1', '1']:
        deviceGroup = N1DeviceGroup
    elif productSelection in ['N2', 'n2', '2']:
        deviceGroup = N2DeviceGroup
    else:
        print 'Invalid product selection done, kindly recheck!'

    whiteListEnabler=raw_input( \
        'Kindly confirm do you want white list function enabled or not!\nYour answer (yes|no):')

    if whiteListEnabler in ['yes', 'Yes', 'YES', 'Y', 'y']:
        rawWhiteList=raw_input( \
            'Kindly input your white listed test case numbers\n(could be string or list format, but not mixed allowed!) :')

#        print '****', rawWhiteList, type(rawWhiteList)
        whiteList = whiteListProcessor(rawWhiteList)
    else:
        whiteList = []

#    whiteList = ['5900.315', '5104.895', '5104.894', '5104.818', '5104.817', '5104.851', '5900.210', '5104.851', \
#                 '5104.116', '5104.944', '5104.945', '5104.946', '5104.947', '5104.951', '5104.826']

#   filter all available test scripts files
    files = listAllFiles(PATH_TO_TEST)
    scriptFiles = removeNonPythonScripts(files)

#   storing all those cases info into list data structures
    for file in scriptFiles:
        groupNo, caseNo, filePath, refPhone = caseFilter(file)
        cases.append((groupNo+'.'+caseNo, filePath, refPhone))

#   for debugging purpose
    debuggingLines()

#   generate the text plan xml file
    composeTestPlan(deviceIDs= deviceGroup, caseList=cases, whiteList=whiteList, debug=False)