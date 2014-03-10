__author__ = 'k22li'

import os

parentPath = r'\Users\k22li\AoL\nst_logs\n2_wk07_basic_adva_mst_120'

print os.path.basename(parentPath)


print os.path.dirname(parentPath)


t = parentPath.split('\\')

for item in t:
    print item