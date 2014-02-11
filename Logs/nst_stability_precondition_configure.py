__author__ = 'k22li'

import os
import os.path as path
from datetime import datetime

SDCARD_SYS_RESTART = r'/storage/sdcard1/logs/upload/SystemRestart'
SDCARD_SYS_TOMBSTONE = r'/storage/sdcard1/logs/upload/SystemTombstone'
SDCARD_APP_CRASH = r'/storage/sdcard1/logs/upload/ApplicationCrash'


#RESULT_PARENT_FOLDER = path.join('c:', 'nst_logs')
#if not os.path.isdir(RESULT_PARENT_FOLDER):
#    os.mkdir(RESULT_PARENT_FOLDER)
#
#os.system('adb -s %s fe')

print type(datetime.now()