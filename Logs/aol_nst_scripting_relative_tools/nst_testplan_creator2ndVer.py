__author__ = 'k22li'
__doc__ = """

Purpose of this test script is to support generate the *.testplan file automatically, which would be used by \
NST environment.

Inputs need to specify:
1) GIT_REPO_ADDRESS  ---> test code
advanced test cases are also repeat configurable for each of the test instance; and the key is that basic & advanced \
test cases should be listed separately.s' local repo
2) mtbfProfile  --->  the configuration files for test cases selection

Outputs:
"*.full.testplan"/"*.mini.testplan" files to be created in your local address


@ difference than 1st version:

"""

import csv
import os
import random
import sets
import re

# to be modified for each different environment separately
GIT_REPO_ADDRESS=r'C:\Users\k22li\workspace\bsta\bsta\cases\cases\test'
#GIT_REPO_ADDRESS=r'C:\Users\k22li\workspace\bsta\bsta\NSTCaseForAthena\cases\test'

# basically no need to change, unless you've to update the test profile manually
mtbfProfile = 'nst_mtbf_testprofile_libra.csv'
#mtbfProfile = 'nst_mtbf_testprofile_athena_wk28.3.csv'
#mtbfProfile = 'nst_mtbf_testprofile_athena_ss_wk28.3.csv'

# basically do not change, unless test environment changed accordingly
RES_PATH=''


def _csvNstMtbfTestProfileWalkThrough(csvFile, testVariant):
    """
    read through the csv NST MTBF test profile and prepare for the case lists
    """
    bas_set = []
    adv_set = []
    mst_set = []
    bad_set = []

    with open(csvFile, 'rb') as profileSeed:
        spamReader = csv.reader(profileSeed)
        for row in spamReader:
            if not row[0] in ["", "Selection"]:
                if row[4].lower() in [testVariant.lower(), 'com']:
                    if row[1].lower() in ['basic'] and _ensureTestScriptAvailableInGit(GIT_REPO_ADDRESS, row[3].rstrip()):
                        bas_set.append(row)

                    elif row[1].lower() in ['advanced'] and _ensureTestScriptAvailableInGit(GIT_REPO_ADDRESS, row[3].rstrip()):
                        for rp in xrange(int(row[5])):
                            adv_set.append(row)

                    elif row[1].lower() in ['mst'] and _ensureTestScriptAvailableInGit(GIT_REPO_ADDRESS, row[3].rstrip()):
                        mst_set.append(row)

#                    elif row[1].lower() in ['ba-adv'] and _ensureTestScriptAvailableInGit(GIT_REPO_ADDRESS, row[3].rstrip()):
#                        bas_set.append(row)
#                        adv_set.append(row)
                    else:
                        bad_set.append(row)

    return bas_set, adv_set, mst_set, bad_set

def _ensureTestScriptAvailableInGit(path, scriptName):
    """
    double check the expected test cases do existing in the current Git repo referred
    """
    assert os.path.isdir(path), "Invalid GIT_REPO_ADDRESS provided for validating test scripts..."
    return os.path.isfile(os.path.join(path,scriptName))

def _checkRefPhoneNeededOrNot(scriptName):

    patten_refPhone = re.compile('self.refPhone|RefHelpers')
    filePath = os.path.join(GIT_REPO_ADDRESS, scriptName.rstrip())

    with open(filePath, 'r+') as script:
        refPhone='False'
        for line in script.readlines():
            if re.search(patten_refPhone, line):
                refPhone='True'

    return refPhone

def _composeTestPlanXml(deviceIDs, testPlanType, basicList, advancedList, mstList, advRandEnabler, advRepeats):

    template='<testcase no="%s" name="" location="%s" refPhone = "%s" loops="%s"/>'

    prefix ="""<?xml version="1.0" encoding="utf-8"?>\n<testplan assignTo="" resultPath="%s" syncQRDLog="true">\n\t<target-device deviceid="%s" device-type="AoL15" outofmemory-flag="True" ref-deviceid="9ddb61ba" ref-device-type="N"/>\n\t<testtask id="1" type="nstrunner" timeout="%s">"""

    taskTemplate='\t</testtask>\n\t<testtask id="%s" type="nstrunner" timeout="%s">'

    postfix = """\t</testtask>\n</testplan>"""

    basicTupleList = []
    advancedTupleList = []
    mstTupleList = []

    if testPlanType.lower() in ['mini', 'm', 'mini-mtbf']:
        for case in basicList:
            basicTupleList.append(tuple(case))
        for case in advancedList:
            advancedTupleList.append(tuple(case))
        for case in mstList:
            mstTupleList.append(tuple(case))

        basicSet = sets.Set(basicTupleList)
        advancedSet = sets.Set(advancedTupleList)
        advancedDeltaList = list(advancedSet.difference(basicSet))
        if advRandEnabler:
            random.shuffle(advancedDeltaList)

        miniCaseList = basicTupleList+advancedDeltaList

        with open('nst_mtbf.mini.testplan', 'w+') as filer:
            filer.write(prefix %(RES_PATH, deviceIDs, 20))
            filer.write('\n')
            for case in miniCaseList:
                refStatus = _checkRefPhoneNeededOrNot(case[3])
                filer.write('\t\t'+template %(case[2], os.path.join(RES_PATH,case[3]),refStatus, 1))
                filer.write('\n')
            filer.write(postfix)

    elif testPlanType.lower() in ['full', 'f', 'full-mtbf']:

        #advancedList = advancedList * int(advRepeats)

        if advRandEnabler:
            random.shuffle(advancedList)

        #print "#"*20, len(advancedList), "#"*20

        with open('nst_mtbf.full.testplan', 'w+') as filer:
            filer.write(prefix %(RES_PATH, deviceIDs, "40"))
            filer.write('\n')
            for case in basicList:
                refStatus = _checkRefPhoneNeededOrNot(case[3])
                filer.write('\t\t'+template %(case[2], os.path.join(RES_PATH,case[3]), refStatus, case[5]))
                filer.write('\n')

            filer.write(taskTemplate %('2', "60"))
            filer.write('\n')

            for case in advancedList:
                refStatus = _checkRefPhoneNeededOrNot(case[3])
                filer.write('\t\t'+template %(case[2], os.path.join(RES_PATH,case[3]), refStatus, 1))
                filer.write('\n')

            filer.write(taskTemplate %('3', "20"))
            filer.write('\n')
            for case in mstList:
                refStatus = _checkRefPhoneNeededOrNot(case[3])
                filer.write('\t\t'+template %(case[2], os.path.join(RES_PATH,case[3]), refStatus, 1))
                filer.write('\n')

            filer.write(postfix)
    else:
            print "Nothing to do .."

    print '*'*30+' Basic Case Number    : %3d '%(len(basicList))+'*'*30
    print '*'*30+' Advanced Case Number : %3d '%(len(advancedList))+'*'*30
    print '*'*30+' MST Case Number      : %3d '%(len(mstList))+'*'*30


if __name__ == '__main__':

    swVariant = raw_input("************* Pls. input the SW variant *************\n(CN/EU) Your selection :")
    if not swVariant.lower()[0] in ['c']:
        swVariant='EU'
    else:
        swVariant='CN'

    testSetType = raw_input("************ To create Full or Mini plan ************\n(Full/Mini) Your Selection:")
    if not testSetType.lower()[0] in ['f']:
        testSetType='mini'
    else:
        testSetType='full'

    randomEnabler = raw_input("****** Enable random order for advanced cases? ******\n(Yes/No) Your selection ")
    if not randomEnabler.lower()[0] in ['y']:
        randomEnabler = False
    else:
        randomEnabler = True

    print ">>>>>>>>>>>>>> Start to generate testplan >>>>>>>>>>>>>>>>>>"

    basicCases, advancedCases, mstCases, nullCases= _csvNstMtbfTestProfileWalkThrough(mtbfProfile,swVariant)

    _composeTestPlanXml("ff0a9e", testSetType, basicCases, advancedCases, mstCases, randomEnabler, 1)

    print ">>>>>>>>>>>>>>> Generate testplan done! >>>>>>>>>>>>>>>>>>>>"

    if len(nullCases):

        print "Bad cases without test scripts available in current repo: "
        for badCase in nullCases:
            print nullCases.index(badCase), ' ---> ', badCase