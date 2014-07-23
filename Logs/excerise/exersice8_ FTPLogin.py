__author__ = 'k22li'

import ftplib
from ftplib import FTP
import warnings
import  os
import string
import random


class FtpBrowser():

    """
    browsing from the FTP
    """
    def __init__(self, host='', port='', user='', passwd=''):
        """
        initialize all elements for FTP login
        """
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd

        self.ftp = FTP()

    def loggingIn(self):
        """
        login
        """
        try:
            self.ftp.connect(host=self.host, port=self.port)
            self.ftp.login(user=self.user, passwd=self.passwd)
        except ftplib.error_reply as e:
#            warnings.warn(e, DeprecationWarning, stacklevel=2)
            pass

    def listDir(self):
        """
        list the files under the current dirs
        """
        self.ftp.dir()

    def debuggingInfo(self, debugStr="DEBUG: "*30):
        """
        print the debugging string
        """
        print debugStr

    def createNewDirsInServerSide(self,*args):
        """
        create new dirs in server side if not existing
        """
        if not len(args):
            warnings.warn('No dir name being provided so far!')

#        existingDirs = self.listDir()

        for item in args:
            if item:
                print item
                self.ftp.cwd('Athena_MTBF')
                self.ftp.mkd(item[:3])
            else:
                self.dupDirs.append(item)
                warnings.warn('dir already existing!')


if __name__ == '__main__':

    ftp = FtpBrowser(host='172.28.187.162', port='2121', user='k22li', passwd='#Kevin83')
    ftp.loggingIn()
    ftp.listDir()

    ftp.createNewDirsInServerSide(string.letters)
    ftp.listDir()


