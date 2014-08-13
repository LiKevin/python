__author__ = 'k22li'

import os

def updateLocalTestCodes(gitRepo):
    if os.path.isdir(gitRepo):
        os.chdir(gitRepo)
        status = os.system('git pull')
    else:
        status = 1

    return status

def uploadTestCasesToRemoteDestination(localScriptPath, remoteScriptPath):

    if os.path.isdir(localScriptPath):
        os.chdir(localScriptPath)
        localScriptFolder = 'cases'
        status = os.system('scp -r %s %s'%(localScriptFolder, remoteScriptPath))
        print '>>>> scripts updating done!'
    else:
        print 'Invalid local script path provided!'
        status = 1

    return status


if __name__=='__main__':

    updateLocalTestCodes(r'C:\Users\k22li\workspace\bsta\bsta')

    print 'done'