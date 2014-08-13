__author__ = 'k22li'

import os
import re

class CrashLogAnalyzer():

    def __init__(self, logPath):

        if not os.path.isdir(logPath):
            raise  IOError, 'invalid path to log files have been assigned!'

        self.logPath = logPath
        self.deviceFolders = []
        self.crashFolderName = 'BYD_CRASHLOG'

    def __call__(self, *args, **kwargs):
        pass

    def getDeviceFolders(self):
#        get all those devices folders inside
        self.deviceFolders.extend(os.listdir(self.logPath))

    def getCrashLogFolders(self, deviceFolder):

        crashLogPath = os.path.join(self.logPath, deviceFolder, self.crashFolderName)
        crashFolders = os.listdir(crashLogPath)
        crashNumber = len(crashFolders)

        return crashFolders

    def getAplogFileName(self, crashPath):
        files = os.listdir(crashPath)
        m = re.match(re.compile('aplog_*'), files)
        if m:
            return m.group(0)

    def searchingCrashPatten(self):

        appCrash = re.compile('am_crash', I)
        appFreeze = re.compile('ANR', I)

        return appCrash, appFreeze

    def analyzeCrashLog(self, aplogName):

        appCrashPattern, appFreezePattern = self.searchingCrashPatten()

        with open(aplogName, 'r+') as f:
            for line in f.readlines():
                if re.search(appCrashPattern, line) or re.search(appCrashPattern, line):
                    return line

    def run(self):
        self.getDeviceFolders()

        for deviceFolder in self.deviceFolders:
            for