__author__ = 'k22li'

import re
import os
import os.path as Path
import sets
import random

#   path to all those available test scripts
PATH_TO_TEST=r'C:\Users\k22li\workspace\bsta\bsta\NSTCaseForAthena\cases\test'
#   path to the test environment where to fetch those test scripts for executions
TARGET_PATH=r'./NSTRunner/cases/test'
#   path to NST test result storage
RES_PATH=r'./TestResult'
#   execution duration for nst runs
EXEC_DURATION='120'
BASIC_EXEC_DURATION='40'
ADVANCED_EXEC_DURATION='60'
MST_EXEC_DURATION = '20'

BASIC_CASES = 'MTBF59000101_HomeScreenSwipeLeftAndRight.py,MTBF59000102_HomeScreenFastlaneBasicUsage.py,MTBF59000103_HomeScreenLockUnlockDevice.py,MTBF59000104_HomeScreenPinUnpinApp.py,MTBF59000201_DualSIMSelectPreferredSIM.py,MTBF59000301_ContactsAddContactInDialer.py,MTBF59000302_ContactsAddContactInContacts.py,MTBF59000303_ContactsDeleteContact.py,MTBF59000401_CreateMOCallViaPB.py,MTBF59000402_CreateMOCallViaDialerAndBeRejected.py,MTBF59000403_ActivateAndDeactivateIHFInMOCall.py,MTBF59000404_Create2GMOCallViaPB.py,MTBF59000405_Create3GMOCallViaPB.py,MTBF59000406_ReceiveAndRejectMTCall.py,MTBF59000407_MuteAndUnmuteActiveMTCall.py,MTBF59000408_ReceiveAndAnswerMTCallIn2GMode.py,MTBF59000409_ReceiveAndAnswerMTCallIn3GMode.py,MTBF59000410_CreateMOCallViaSIM2.py,MTBF59000501_SendSMSToRemotePhone.py,MTBF59000502_SendAndReceiveSMSIn2GMode.py,MTBF59000503_SendAndReceiveSMSIn3GMode.py,MTBF59000504_ReceiveMMSFromRemoteAndOpenIt.py,MTBF59000505_SendPictureMMSToOwnNumber.py,MTBF59000506_ReplyWithSMSToReceivedMMS.py,MTBF59000507_DeleteLatestReceivedMMS.py,MTBF59000508_SendMMSWithImageToRemotePhone2G.py,MTBF59000509_SendMMSWithNewImageToRemotePhone3G.py,MTBF59000510_OpenUpdateAndCloseEmail.py,MTBF59000511_SendReceiveEmailVia2G.py,MTBF59000512_ShareImageFromGalleryViaEmail.py,MTBF59000513_SendReceiveEmailWithAttachmentVia3G.py,MTBF59000601_CaptureImage.py,MTBF59000602_ZoomAndCaptureImage.py,MTBF59000603_CaptureVideo.py,MTBF59000701_VideoPlaybackControl.py,MTBF59000801_OpenCapturedPhotoFromGallery.py,MTBF59000802_PinchZoomAPhotoInGallery.py,MTBF59000803_SetImageAsWallpaper.py,MTBF59000804_DeleteImageFromGallery.py,MTBF59000901_BrowseToAWebPage.py,MTBF59001001_PlayMusicViaMusicPlayer.py,MTBF59001201_OpenAndStartANewGame.py,MTBF59001202_SetAlarmAndWaitForExpiration.py,MTBF59001401_SwitchBTOnOffViaNotificationDrawer.py,MTBF59001402_SearchAvailableBluetoothDevices.py,MTBF59001403_SendDataViaBluetooth.py,MTBF59001404_SetMobileDataOnOffViaNotificationDrawer.py,MTBF59001405_SwitchWLANOnOffViaNotificationDrawer.py,MTBF59001406_SearchForWLANNetworks.py,MTBF59001501_MapsBasicOptions.py,MTBF59001301_RadioOnOff.py,MTBF59001302_RadioTuning.py,MTBF59001203_DownloadAnAppFromStoreAndUseIt.py,MTBF59001204_AddAppointmentToCalendar.py,MTBF59001205_EditCalendarAppointment.py,MTBF59001206_AddAppointmentToCalendarAndRemoveViaFastLane.py,MTBF59001101_ChangeRingtone.py,MTBF59001102_ChangeScreenBrightness.py,MTBF59000902_VideoStreamingViaWLAN.py,MTBF59000903_PinchZoomAWebPage.py,MTBF59000904_ReceiveMTCallWhileBrowsing.py,MTBF59000905_BrowseToAWebPageVia2G.py,MTBF59000906_BrowseToAWebPageViaBookmarksVia3G.py,MTBF59000907_VideoStreaming3G.py,MTBF59000910_BrowseToAWebPage_Opera.py,MTBF59000911_VideoStreamingViaWLAN_Opera.py,MTBF59000912_PinchZoomAWebPage_Opera.py,MTBF59000913_ReceiveMTCallWhileBrowsing_Opera.py,MTBF59000914_BrowseToAWebPageVia2G_Opera.py,MTBF59000915_BrowseToAWebPageViaBookmarksVia3G_Opera.py,MTBF59000916_VideoStreaming3G_Opera.py'
#BASIC_CASES = 'MTBF59000101_HomeScreenSwipeLeftAndRight.py,MTBF59000102_HomeScreenFastlaneBasicUsage.py,MTBF59000103_HomeScreenLockUnlockDevice.py,MTBF59000104_HomeScreenPinUnpinApp.py,MTBF59000201_DualSIMSelectPreferredSIM.py,MTBF59000301_ContactsAddContactInDialer.py,MTBF59000302_ContactsAddContactInContacts.py,MTBF59000303_ContactsDeleteContact.py,MTBF59000401_CreateMOCallViaPB.py,MTBF59000402_CreateMOCallViaDialerAndBeRejected.py,MTBF59000403_ActivateAndDeactivateIHFInMOCall.py,MTBF59000404_Create2GMOCallViaPB.py,MTBF59000405_Create3GMOCallViaPB.py,MTBF59000406_ReceiveAndRejectMTCall.py,MTBF59000407_MuteAndUnmuteActiveMTCall.py,MTBF59000408_ReceiveAndAnswerMTCallIn2GMode.py,MTBF59000409_ReceiveAndAnswerMTCallIn3GMode.py,MTBF59000410_CreateMOCallViaSIM2.py,MTBF59000501_SendSMSToRemotePhone.py,MTBF59000502_SendAndReceiveSMSIn2GMode.py,MTBF59000503_SendAndReceiveSMSIn3GMode.py,MTBF59000504_ReceiveMMSFromRemoteAndOpenIt.py,MTBF59000505_SendPictureMMSToOwnNumber.py,MTBF59000506_ReplyWithSMSToReceivedMMS.py,MTBF59000507_DeleteLatestReceivedMMS.py,MTBF59000508_SendMMSWithImageToRemotePhone2G.py,MTBF59000509_SendMMSWithNewImageToRemotePhone3G.py,MTBF59000510_OpenUpdateAndCloseEmail.py,MTBF59000511_SendReceiveEmailVia2G.py,MTBF59000512_ShareImageFromGalleryViaEmail.py,MTBF59000513_SendReceiveEmailWithAttachmentVia3G.py,MTBF59000601_CaptureImage.py,MTBF59000602_ZoomAndCaptureImage.py,MTBF59000603_CaptureVideo.py,MTBF59000701_VideoPlaybackControl.py,MTBF59000801_OpenCapturedPhotoFromGallery.py,MTBF59000802_PinchZoomAPhotoInGallery.py,MTBF59000803_SetImageAsWallpaper.py,MTBF59000804_DeleteImageFromGallery.py,MTBF59000901_BrowseToAWebPage.py,MTBF59001001_PlayMusicViaMusicPlayer.py,MTBF59001201_OpenAndStartANewGame.py,MTBF59001202_SetAlarmAndWaitForExpiration.py,MTBF59001401_SwitchBTOnOffViaNotificationDrawer.py,MTBF59001402_SearchAvailableBluetoothDevices.py,MTBF59001403_SendDataViaBluetooth.py,MTBF59001404_SetMobileDataOnOffViaNotificationDrawer.py,MTBF59001405_SwitchWLANOnOffViaNotificationDrawer.py,MTBF59001406_SearchForWLANNetworks.py,MTBF59001501_MapsBasicOptions.py,MTBF59001301_RadioOnOff.py,MTBF59001302_RadioTuning.py,MTBF59001203_DownloadAnAppFromStoreAndUseIt.py,MTBF59001204_AddAppointmentToCalendar.py,MTBF59001205_EditCalendarAppointment.py,MTBF59001206_AddAppointmentToCalendarAndRemoveViaFastLane.py,MTBF59001101_ChangeRingtone.py,MTBF59001102_ChangeScreenBrightness.py,MTBF59000902_VideoStreamingViaWLAN.py,MTBF59000903_PinchZoomAWebPage.py,MTBF59000904_ReceiveMTCallWhileBrowsing.py,MTBF59000905_BrowseToAWebPageVia2G.py,MTBF59000906_BrowseToAWebPageViaBookmarksVia3G.py,MTBF59000907_VideoStreaming3G.py,MTBF59000910_BrowseToAWebPage_Opera.py, MTBF59000911_VideoStreamingViaWLAN_Opera.py	MTBF59000912_PinchZoomAWebPage_Opera.py, MTBF59000913_ReceiveMTCallWhileBrowsing_Opera.py, MTBF59000914_BrowseToAWebPageVia2G_Opera.py, MTBF59000915_BrowseToAWebPageViaBookmarksVia3G_Opera.py, MTBF59000916_VideoStreaming3G_Opera.py'
BASIC_EXEC_TUPLE = BASIC_CASES.split(',')
USELESS_SCRIPTS = ['testPoxReferencePhone.py', 'bluetoothSetting.py']
#######################################################################################################################
#Sub-Functions
#######################################################################################################################
def listAllFiles(path):

    if os.path.isdir(path):
        return os.listdir(path)
    else:
        return ''

def removeNonPythonScripts(fileList):

    for file in fileList:
        if not (file.startswith('MTBF') and file.endswith(".py")):
            fileList.remove(file)

    return fileList

#    if '__init__.py' in fileList:
#        fileList.remove('__init__.py')
#    return fileList

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

    template='<testcase no="%s" name="" location="%s" refPhone = "%s" loops="10"/>'

    prefix ="""<?xml version="1.0" encoding="utf-8"?>\n<testplan assignTo="%s" resultPath="%s" syncQRDLog="true">\n\t<target-device hwversion="" osversion="" deviceid=""/>\n\t<testtask id="1" type="nstrunner" timeout="%s">"""

    taskTemplate='\t</testtask>\n\t<testtask id="%s" type="nstrunner" timeout="%s">'

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
    AthenaDeviceGroup = 'ff09db'

    productSelection = raw_input( \
        'Would you like to create testplan.xml for N1 or N2 or Athena?\nYour answer (n1 | n2| athena) : ')

    if productSelection in ['N1', 'n1', '1']:
        deviceGroup = N1DeviceGroup
    elif productSelection in ['N2', 'n2', '2']:
        deviceGroup = N2DeviceGroup
    elif productSelection in ['Athena', 'athena', 'aol3']:
        deviceGroup = AthenaDeviceGroup
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
        'Do you want to enable the randomize sorting of the Advanced test    executions?\nYour answer (yes|no) : ')

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