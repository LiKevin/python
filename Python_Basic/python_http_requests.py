__author__ = 'k22li'

import requests
from xml.etree import ElementTree

def requestNewUrl():
    urlLink = raw_input('Kindly provide the url address to sync: ')
    req = requests.get(urlLink)
    if not req.status_code == 200:
        print 'failed to request the url page: %s'%urlLink
    return req.text, req.encoding

def xmlParseDownloadedPages(strings, encodingMethod):
    if not isinstance(strings, unicode):
        print 'not this string is encoded via utf-8'
        strings = strings.decode(encodingMethod) # decode the dumped contents via the encoding methods
        strings = strings.encode('utf-8')
    else:
        print encodingMethods
        print 'validate if the string dumped belongs to unicode instance or not: ', isinstance(strings, unicode)
        print 'check if the content is kind of string or not: ', isinstance(strings, str)
        strings = strings.encode('utf-8')
        print 'check if the content is kind of string or not: ', isinstance(strings, str)
        print strings
#        strings = strings.decode(encodingMetho)
    tree = ElementTree.fromstring(strings)
    print tree.tag
#    print tree.getroot()
#    tree.getroot()
#    print ElementTree.iselement(tree)

urlContent, encodingMethods = requestNewUrl()
xmlParseDownloadedPages(urlContent, encodingMethods)





