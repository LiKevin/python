__author__ = 'k22li'

import re
import os
import os.path as Path
import sets
import random

#   path to all those available test scripts
PATH_TO_TEST=r'C:\Users\k22li\workspace\bsta\bsta\cases\test'
#   path to the test environment where to fetch those test scripts for executions
TARGET_PATH=r'/home/nst/NSTRunner/cases/test'
#   path to NST test result storage
RES_PATH=r'/home/nst/TestResult'
#   execution duration for nst runs
EXEC_DURATION='120'
BASIC_EXEC_DURATION='40'
ADVANCED_EXEC_DURATION='60'
MST_EXEC_DURATION = '20'

#BASIC_EXEC_TUPLE = ('addAppointment.py', 'addAppointmentToCalendar.py', 'addCalendarToActivityScreen.py', 'deleteAppointmentInTheCalendar.py', 'bluetoothSetting.py', 'call_fastlane.py', 'callFromMadeList.py', 'callFromMissedList.py', 'callFromPhonebook.py', 'callFromRecvList.py', 'changeWP.py', 'closeMusicPlayer.py', 'dataConn.py', 'listenDownloadedRingTone.py', 'downloadAndSetRingTone.py', 'deleteDownloadRingTone.py', 'downloadImageAndSetWallpaper.py', 'deleteDownloadedImage.py', 'downloadJavaApp.py', 'deleteDownloadedJavaApp.py', 'downloadVideoWithDRM.py', 'deleteDownloadedVideo.py', 'sendMMSWithAudio.py', 'openMMSWithAudio.py', 'sendMMSWithPic.py', 'openMMSWithImage.py', 'sendMMSWithVideo.py', 'openMMSWithVideo.py', 'sendSegSMS.py', 'openAndCloseRadio.py', 'openAndPlaybackDownloadedVideo.py', 'openBrowser.py', 'openDownloadedImage.py', 'deleteDownloadedImage.py', 'openDownloadedVideo.py', 'deleteDownloadedVideo.py', 'openEmail.py', 'openMusicPlayer.py', 'takePicture.py', 'openPicGallery.py', 'deletePicGallery.py', 'recordVideo.py', 'playVideoFromGallery.py', 'deleteVideoGallery.py', 'setAnAlarm.py', 'deleteAllAlarm.py', 'openPreloadGame.py', 'openSMS.py', 'addContact.py', 'deleteContact.py', 'ebuddy.py', 'javagame.py', 'mute_notification.py', 'navigateToLink.py', 'wifi_notification.py', 'playMusic.py', 'playVideoStreamingContentUsingDeviceBrowserAndVideoPlayer.py', 'recvCall.py', 'wifi_search.py', 'createDrafMail.py', 'sendEmail.py', 'createDrafMail.py', 'sendEmailWithAttach.py', 'setWallpaper.py', 'silentProfile.py', 'sms_fastlane.py', 'wlanFromSetting.py', 'data_settings.py')
BASIC_CASES = 'calc.py , callFromPhonebook.py , callFromRecvList.py , callFromMadeList.py , callFromMissedList.py , recvCall.py , addContact.py , deleteContact.py , sendSegSMS.py , openSMS.py , sendMMSWithAudio.py , openMMSWithAudio.py , sendMMSWithVideo.py , openMMSWithVideo.py , sendMMSWithPic.py , openMMSWithImage.py , openBrowser.py , downloadAndSetRingTone.py , deleteDownloadRingTone.py , downloadImageAndSetWallpaper.py , deleteDownloadedImage.py , downloadVideoWithDRM.py , deleteDownloadedVideo.py , downloadJavaApp.py , deleteDownloadedJavaApp.py , listenDownloadedRingTone.py , openDownloadedImage.py , openAndPlaybackDownloadedVideo.py , addAppointmentToCalendar.py , addCalendarToActivityScreen.py , deleteAppointmentInTheCalendar.py , setAnAlarm.py , deleteAllAlarm.py , recordVideo.py , playVideoFromGallery.py , deleteVideoGallery.py , takePicture.py , openPicGallery.py , deletePicGallery.py , call_fastlane.py , sms_fastlane.py , openAndCloseRadio.py , playVideoStreamingContentUsingDeviceBrowserAndVideoPlayer.py , openMusicPlayer.py , playMusic.py , closeMusicPlayer.py , openPreloadGame.py , javagame.py , setWallpaper.py , changeWP.py , ebuddy.py , sendEmail.py , sendEmailWithAttach.py , createDrafMail.py , openEmail.py , bt_settings.py , wifi_settings.py , wifi_search.py , wifi_notification.py , bluetoothSetting.py , data_settings.py , data_notification.py , mute_notification.py , testPoxReferencePhone.py'
BASIC_EXEC_TUPLE = BASIC_CASES.split(' , ')
#USELESS_SCRIPTS = ['BlackScreen.py', 'calc01.py', 'calc2.py', 'rpcCall.py', 'settingsSample.py', 'test_scenario3.py', 'inputTest.py', 'phoneCall_PlayMusic.py', 'testPoxReferencePhone.py', 'listenDownloadedRing.py', 'deleteDownloadedRing.py', 'test.py', 'bt_settings.py', 'wifi_settings.py', 'data_notification.py']
USELESS_SCRIPTS = []

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

def composeTestPlan(deviceIDs, caseList, randomizeEnable, whiteList, debug):

    template='<testcase no="%s" name="" location="%s" refPhone = "%s"/>'

    prefix ="""<?xml version="1.0" encoding="utf-8"?>\n<testplan assignTo="%s" resultPath="%s" syncQRDLog="true">\n\t<target-device hwversion="" osversion="" deviceid=""/>\n\t<testtask id="1" type="monkeyrunner" timeout="%s">"""

    taskTemplate='\t</testtask>\n\t<testtask id="%s" type="monkeyrunner" timeout="%s">'

    postfix = """\t</testtask>\n</testplan>"""

    basicSet = []
    advancedSet = []
    mstSet = []

#   take 5900 as basic group number; while 5104 as advanced number
    if whiteList:
        pass
    else:
        whiteList = caseList

    caseListSet = sets.Set(caseList)
    whiteListSet = sets.Set(whiteList)

    for case in list(caseListSet.intersection(whiteListSet)):
        if case[0].startswith('59'):
            basicSet.append(case)
        elif case[0].startswith('51'):
            advancedSet.append(case)
        else:
            mstSet.append(case)

#   sorting the basic test cases according to the known order and the MST test cases as well
    basicSet, invalidSet = sortBasicCasesAccordingList(basicSet, BASIC_EXEC_TUPLE, USELESS_SCRIPTS)
    mstSet.sort()

    if randomizeEnable:
        random.shuffle(advancedSet)


    if debug:
        print prefix %(deviceIDs, RES_PATH, BASIC_EXEC_DURATION)
        for case in basicSet:
            print '\t\t'+template %(case[0], case[1], case[2])

        print taskTemplate %('2', ADVANCED_EXEC_DURATION)
        for case in advancedSet:
            print '\t\t'+template %(case[0], case[1], case[2])

        print taskTemplate %(3, MST_EXEC_DURATION)
        for case in mstSet:
            print '\t\t'+template %(case[0], case[1], case[2])

        print postfix

    else:
        with open('testplan.xml', 'w+') as filer:
            filer.write(prefix %(deviceIDs, RES_PATH, BASIC_EXEC_DURATION))
            filer.write('\n')
            for case in basicSet:
                filer.write('\t\t'+template %(case[0], case[1], case[2]))
                filer.write('\n')

            filer.write(taskTemplate %('2', ADVANCED_EXEC_DURATION))
            filer.write('\n')
            for case in advancedSet:
                filer.write('\t\t'+template %(case[0], case[1], case[2]))
                filer.write('\n')

            filer.write(taskTemplate %('3',MST_EXEC_DURATION))
            filer.write('\n')
            for case in mstSet:
                filer.write('\t\t'+template %(case[0], case[1], case[2]))
                filer.write('\n')

            filer.write(postfix)

    print '*'*30+' Basic Case Number    : %3d '%(len(basicSet))+'*'*30
    print '*'*30+' Advanced Case Number : %3d '%(len(advancedSet))+'*'*30
    print '*'*30+' MST Case Number      : %3d '%(len(mstSet))+'*'*30

def whiteListProcessor(rawList):

    if  len(rawList):
        if rawList.startswith('['):
            whiteList = eval(rawList)
        else:
            whiteList = re.split(r'[\[,;\s\n\]]\s*', rawList)
    else:
        print 'Kindly check the "RawList" provided, which might not in good format: %s' %rawList

    return whiteList

def sortBasicCasesAccordingList(cases, execList, obsoleteList=None):

    caseDict = {}
    for case in cases:
        caseName = case[1].replace(TARGET_PATH+'/', '')
        #   clean up those obsoleted test scripts
        if caseName in obsoleteList:
#            cases.remove(case)
            pass
        else:
            caseDict.update({caseName : case})
        #    print caseDict

    caseDictKeySet = sets.Set(caseDict.keys())
    execListKeySet = sets.Set(list(execList))
#    commonCases = list(execListKeySet.intersection(caseDictKeySet))
    missedBasicCases = list(execListKeySet.difference(caseDictKeySet))

    newCaseList = []
    for item in execList:
        if item not in missedBasicCases:
            newCaseList.append(caseDict[item])

    return newCaseList, missedBasicCases

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
        'Would you like to create testplan.xml for N1 or N2?\nYour answer (n1 | n2) : ')

    if productSelection in ['N1', 'n1', '1']:
        deviceGroup = N1DeviceGroup
    elif productSelection in ['N2', 'n2', '2']:
        deviceGroup = N2DeviceGroup
    else:
        print 'Invalid product selection done, kindly recheck!'

    whiteListEnabler=raw_input( \
        'Kindly confirm do you want white list function enabled or not!\nYour answer (yes|no) : ')

    if whiteListEnabler in ['yes', 'Yes', 'YES', 'Y', 'y']:
        rawWhiteList=raw_input( \
            'Kindly input your white listed test case numbers\n(could be string or list format, but not mixed allowed!) : ')

#        print '****', rawWhiteList, type(rawWhiteList)
        whiteList = whiteListProcessor(rawWhiteList)
    else:
        whiteList = []

    enableRandomize = raw_input( \
        'Do you want to enable the randomize sorting of the Advanced test executions?\nYour answer (yes|no) : ')

    if enableRandomize.startswith('Y') or enableRandomize.startswith('y'):
        enableRandomize = True
    else:
        enableRandomize = False
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
    composeTestPlan(deviceIDs= deviceGroup, caseList=cases, randomizeEnable=enableRandomize, whiteList=whiteList, debug=False)
