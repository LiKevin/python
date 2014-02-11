__author__ = 'k22li'

from datetime import datetime

print str(datetime.today()).split('.')[0].replace(' ', '_').replace(':', '_')
