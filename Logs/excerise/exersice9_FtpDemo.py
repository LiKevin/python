__author__ = 'k22li'

from ftplib import FTP
import ftplib
import os
import sys

CONST_HOST = "172.28.187.162"
CONST_PORT = 2121
CONST_USER = 'k22li'
CONST_PASSWD = '#Kevin83'
CONST_BUFFER = 8196

def connect():

    try:
        ftp = FTP()
        ftp.connect(CONST_HOST, CONST_PORT)
        ftp.login(user = CONST_USER, passwd = CONST_PASSWD)
        ftp.getwelcome()
        return ftp
    except ftplib.all_errors as e:
        sys.stdout.write(e)
        sys.stdout.write('FTP is unavailable, pls. check the host, username & password!'+'\n')
        sys.exit(0)

def disconnect(ftp):

    ftp.quit()


def upload(ftp, filePath):

    f = open(filePath,'rb')
    file_name = os.path.basename(filePath)
    try:
        ftp.storbinary('STOR %s'%file_name, f, CONST_BUFFER)
    except ftplib.error_perm:
        return False
    return True

def download(ftp, filename):

    f = open(filename, 'wb').write
    try:
        ftp.retrbinary('RETR %s'%filename, f, CONST_BUFFER)
    except ftplib.error_perm:
        return False
    return True

def list(ftp):

    ftp.dir()

def find(ftp, file_name):

    exist_file = ftp.nlst()
    if file_name in exist_file:
        return True
    else:
        return False

def changeDir(ftp, destPath):

    ftp.cwd(destPath)

if __name__ == '__main__':

    ftp = connect()
#    list(ftp)

    changeDir(ftp, 'Athena_MTBF/abc')
#    list(ftp)

    if not find(ftp, 'exersice8_ FTPLogin.py'):
        upload(ftp, 'exersice8_ FTPLogin.py')
    else:
        sys.stdout.write('Existing files already!'+"\n")

    list(ftp)

#    for item in os.listdir(os.getcwd()):
#        upload(ftp, item)
#
#    list(ftp)

    print find(ftp, 'exersice8_ FTPLogin.py')
    disconnect(ftp)