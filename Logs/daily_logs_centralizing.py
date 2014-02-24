__author__ = 'k22li'

import os
import sys
import re
import subprocess
import shutil

def scpDailyCrashLogsToLocal(remote, local, productType):
    if not os.path.isdir(local):
        try:
            os.mkdir(local)
        except IOError, e:
            safe_print('>>>> You\'ve met some problem when creating the folder: %s'%local)

#    print 'scp -r %s %s'%(remote, local)
    os.chdir(local)
    subprocess.Popen('scp -r %s/%s_* ./' %(remote, productType))
#    subprocess.Popen('scp -r %s/%s_* ./'%(remote, productType))

    safe_print('>>>> Copy done!')

def safe_print(comment):
    sys.stdout.write(comment)
    sys.stdout.flush()

def getAllCrashLogFolders(pPath, productType):
    productType = productType.lower()
    crashLogFolders = []
    if os.path.isdir(pPath):
        folderNames = os.listdir(pPath)

        crashLogFolders = map(lambda folderName :  re.match(re.complie(productType), folderName).group(0), folderNames)

    return crashLogFolders

if __name__=='__main__':

    remoteN1ParentPath = 'k22li@10.233.7.215:~/N/NST_Home/TestResult'
    remoteN2ParentPath = 'root@10.233.19.232:/home/nst/TestResult'

    localParentPath = r'c:/Users/k22li/AoL/nst_logs'
#    localParentPath = os.path.join('c:\\', 'Users', 'k22li', 'AoL', 'nst_logs')

    productType = raw_input( \
        '>>>> Kindly let me know the product you want to tracking.\nYour answer (n1|n2) : ')

    if productType in ['n1', 'N1', '1']:
        remotePath = remoteN1ParentPath
    else:
        remotePath = remoteN2ParentPath
#
#    crashLogFolders = getAllCrashLogFolders(remotePath, productType)
#    print crashLogFolders
#
#    for subfolder in crashLogFolders:
#        remoteTargetPath = os.path.join(remotePath, subfolder)
    scpDailyCrashLogsToLocal(remotePath, localParentPath, productType)

