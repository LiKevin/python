__author__ = 'k22li'

import os
#import warnings
import shutil
import time
from datetime import datetime
from crashlog_summary import NstResultSummary

BYD_CRASHLOG=r'/data/logs/crashlog%s'
BYD_TOMBSTONE=r'/data/tombstones/'
BYD_HISTORYEVENT=r'/data/logs/history_event'
BYD_ANR=r'/data/anr' #FIXME: to be double confirm on the path

QCOM_STORAGE_LOGS=r'/storage/sdcard1/logs'

N1_DEVICE_IDS=['a030623e','b3b9521d','1a2215a']
N2_DEVICE_IDS="995b62e7,995b62f9,995b6330,995b63d2,99626218".split(',')

VALID_ERR_TYPES=['BYD_CRASHLOG', 'BYD_TOMBSTONE', 'BYD_HISTORYEVENT', 'BYD_ANR', 'QCOM_STORAGE_LOGS']

#print N2_DEVICE_IDS

def fetchPhoneCrashLogs(deviceIds=[]):

    print '*'*80+'\tStart to fetch logs from devices\t'+'*'*80

    for eachDevice in deviceIds:
#        Create the device level log folders
        try:
            if not os.path.isdir(os.path.join(os.curdir, eachDevice)):
                os.mkdir(os.path.join(os.curdir, eachDevice))
            else:
    #            warnings.showwarning(\
                print( \
                    'There is already directory exist in your destination, are you sure to OVERWRITE?')
                answer = raw_input('(yes,no):')
                if answer in ['Yes', 'yes', 'YES', 'Y', 'y']:

                    shutil.rmtree(os.path.join(os.curdir, eachDevice), ignore_errors=True)
    #                os.rmdir(os.path.join(os.curdir, eachDevice))
                    time.sleep(5)
                    counter = 5
                    while counter >0:
                        if not os.path.isdir(os.path.join(os.curdir, eachDevice)):
                            os.mkdir(os.path.join(os.curdir, eachDevice))
                            break
                        else:
                            print 'Directory cleaning up is still ongoing... waiting...'
                            time.sleep(5)
                        counter -= 1

                else:
    #                warnings.showwarning(\
                    print( \
                        'You\' selected to cancel this action!')
                    break
            for eachErrType in VALID_ERR_TYPES:
                os.mkdir(os.path.join(os.curdir, eachDevice, eachErrType))
                if eachErrType in ['BYD_CRASHLOG']:
                    errCounter = 0
                    for i in range(6):
                        try:
                            resp = os.system( \
                                'adb -s %s pull %s %s' %(eachDevice, \
                                                        eval(eachErrType)%str(i), \
                                                        os.path.join(os.curdir, eachDevice, \
                                                            eachErrType, 'crashlog'+str(i))))
                            if resp >0:
                                errCounter += 1
                        except SystemExit:
                            pass
                else:
                    try:
                        errCounter=0
                        resp=os.system('adb -s %s pull %s %s' %(eachDevice, eval(eachErrType), \
                                                           os.path.join(os.curdir, eachDevice, eachErrType)))
                        if resp>0:
                            errCounter+=1

                    except SystemExit:
                        pass
        except:
            print 'Bad adb connections to %s' %eachDevice

    print '*'*80+'\tDone\t'+'*'*80

def printDebuggingWindow(comment):
    commentLen = len(comment)
    print '#'*(commentLen+4)
    print '# %s #' %comment
    print '#'*(commentLen+4)


if __name__=='__main__':

#    LOG_PARENT_DIR=r'C:\Users\k22li\workspace\gitHub\Python_Projects\python\Logs'
    homeDir=os.curdir
#    print homeDir

    product = raw_input( \
            'You are about to fetch crash logs from phone, kindly provide your product info firstly!\n\r(n1/n2):')

    date_folder = product+'_'+str(datetime.today()).split('.')[0].replace(' ', '_').replace(':', '_')
    new_dir = os.path.join(os.curdir, date_folder)
    os.mkdir(new_dir)
    os.chdir(new_dir)
    if product in ['N1', 'n1', '1']:
        fetchPhoneCrashLogs(N1_DEVICE_IDS)
        folderBlackList = N1_DEVICE_IDS
    elif product in ['N2', 'n2', '2']:
        fetchPhoneCrashLogs(N2_DEVICE_IDS)
        folderBlackList = N2_DEVICE_IDS
    else:
        print '*'*80+'Wrong inputs, abort log fetching!'+'*'*80

#    print '#'*160, '\n\r# %s\n\r' %'RESULTS UNDER ANALYSIS...', '#'*160
    os.chdir('..')
    printDebuggingWindow(comment='RESULTS UNDER ANALYSIS...')
    summarizer = NstResultSummary()
    summarizer(homeDir, folderBlackList)