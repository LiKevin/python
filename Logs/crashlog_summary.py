__author__ = 'k22li'

import re
import os

class NstResultSummary():

    def __init__(self):
        pass

    def __call__(self, homeDir, folderBlackList):
        self.logHomeDir = homeDir
        self.listDirs(homeDir, folderBlackList)

    def listDirs(self, homeDir, folderBlackList):
        dayFolders=[]
        rawFileList=os.listdir(homeDir)
        folderBlackList.extend(['.', '..', 'final'])
    #   get rid of any files or cur/ parent folders
        for item in rawFileList:
            if os.path.isdir(os.path.join(self.logHomeDir, item)) and item not in folderBlackList:
                dayFolders.append(item)

    #   take care of the parent dirs if there is
        for dayFolder in dayFolders:
            deviceIds=os.listdir(os.path.join(self.logHomeDir, dayFolder))
            try:
                deviceIds.__delitem__('.')
                deviceIds.__delitem__('..')
            except:
                pass


            for eachDevice in deviceIds:
                print '*'*30+'\tStart to analyze history logs from device: %s\t' %eachDevice+'*'*30
                with open(os.path.join(self.logHomeDir,dayFolder, eachDevice, 'BYD_HISTORYEVENT', 'history_event')) as histFile:

    #             with open(os.path.join(self.logHomeDir,dayFolder, 'BYD_HISTORYEVENT','history_event')) as histFile:

                    for line in histFile.readlines():
    #                    print line.strip().split('  '), len(line.strip().split('  '))
                        lineElements=line.strip().split('  ')
                        if len(lineElements) == 4:
                            if re.search('(TOMB|CRASH|ANR|SYSTEMRESTART)', lineElements[3], flags=0):
                                print lineElements


if __name__=='__main__':

    logHomeDir=r'C:\Users\k22li\workspace\gitHub\Python_Projects\python\Logs'
    t=NstResultSummary()
    t(logHomeDir)
