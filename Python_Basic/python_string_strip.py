__author__ = 'k22li'

import re
url = 'www.cnn.com'

print url.strip('wcom.')

print url.rstrip('wcom.')

print url.lstrip('wcom.')

print re.match('www.(.*).com',url).group(1)