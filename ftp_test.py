__author__ = 'k22li'

import os, sys, shutil
from ftplib import FTP
import re

ftp = FTP("betstas02.china.nokia.com")
#ftp.login('anonymous',"boush.1.li@nokia.com")

ftp.login('anonymous',"kevin.4.li@nokia.com")
#ftp.dir()
#print '*'*20
#ftp.cwd("granite/test_data")
#ftp.dir()
#
#print ftp.pwd()

print ftp.getwelcome()
#print ftp.getline()
#print ftp.file
#print ftp.retrlines('LIST')
ftp.cwd('granite')
print ftp.retrlines('NLST')
ftp.cwd('test_data')
#print ftp.retrlines('LIST')


#ftp.mkd('test_kevin')
#print ftp.retrlines('LIST')

#ftp.cwd('test_kevin')
#print ftp.retrlines('LIST')
t = ftp.dir('')
print '*'*80
print t