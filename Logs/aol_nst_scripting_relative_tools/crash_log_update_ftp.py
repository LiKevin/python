__author__ = 'k22li'


# This script using for upload test data for Granite

import os, sys

def upload(source_path):
    from ftplib import FTP
#    ftp=FTP("betstas02.china.nokia.com")
#    #ftp=FTP("10.233.19.102")
#    ftp.login("anonymous", "boush.1.li@nokia.com")
#    directory = "granite/test_data"
    ftp=FTP()
    ftp.connect("10.233.7.215","2121")
    ftp.login("k22li", "#Jiangke86")
    directory = "/srv/ftp/upload"

    ftp.cwd(directory)
    if os.path.isdir(source_path):
        for root, dirs, files in os.walk(source_path):

        if files:
            for file in files:
                full_path = os.path.join(root, file)
                with open(full_path, 'rb') as f:
                    safe_print(">>> Uploading " + file)
                    tmpPath = root.replace(r'C:\Users\k22li\AoL\nst_logs\n1_wk07_basic_adva_mst_120', '')
                    try:
                        ftp.cwd(tmpPath)
                    except:
                    #                            print 'failed to find the root'
                        tmpPathElems = tmpPath.split('\\')
                        for elem  in tmpPathElems:
                            try:
                                ftp.cwd(elem)
                            except:
                            #                                    print 'failed to navigate to folder %s'%elem
                                try:
                                    ftp.mkd(elem)
                                    #                                        ftp.
                                    ftp.cwd(elem)
                                #                                        print 'new dir created'
                                except:
                                    print 'failed to create dir'
                    print (directory+tmpPath.replace('\\', '/'))

                    ftp.cwd(directory+tmpPath.replace('\\', '/'))
                    ftp.storbinary('STOR ' + file, f, 1024 * 1024)
                    ftp.cwd('/srv/ftp/upload')
    ftp.cwd('/srv/ftp/upload')
    ftp.quit()
else:
#file = open(source_path, 'rb')
        with open(source_path, 'rb') as f:
            safe_print(">>> Uploading " + source_path)
            ftp.storbinary('STOR ' + os.path.basename(source_path), f, 1024 * 1024)
    safe_print(">>> Upload test data completely...")
    return None

def safe_print(text):
    sys.stdout.write(text + '\n')
    sys.stdout.flush()

sourcePath = os.path.join('C:\\', 'Users', 'k22li', 'AoL', 'nst_logs', 'n1_wk07_basic_adva_mst_120')

print sourcePath

if __name__ == '__main__':
    try:
        if os.path.exists(sourcePath):
            upload(sourcePath)

#            for root, dirs, files in os.walk(sourcePath)
#                print root, dirs, files
        else:
            print(">>> Please input correct path.")
            print(">>> Maybe need using '/' instead '\\' in path str.")
    except IndexError:
        print(">>> Run this script like this:")
        print(">>> ipy upload_testdata.py source_path")
