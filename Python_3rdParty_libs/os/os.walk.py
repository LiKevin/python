__author__ = 'k22li'

import os

parentPath = r'C:\Users\k22li\AoL\nst_logs\n2_wk07_basic_adva_mst_120'
for root, dirs, files in os.walk(parentPath, False):

    for file in files:
        print root
        print os.path.join(root, file)

