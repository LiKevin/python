__author__ = 'k22li'

import sys, subprocess, os

os.system("ssh root@10.220.120.236 'for device in `adb devices|awk {print $1}`; do echo $device; done'")
