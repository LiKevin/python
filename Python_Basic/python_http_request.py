__author__ = 'k22li'

import requests
from xml.etree import ElementTree

def requestUrlResources():
    """
     request resources from the targe urls
    """
    urlToVisit = raw_input('Pls. give your web address to visit: ')
    req = requests.request('GET', urlToVisit)
    return req.text

def encodingRequestedConents(contents = '', coding = 'gb2312'):
    """
    decode the page contents in case there are illegal encodings
    """
    if not isinstance(contents, unicode):
        print 'non-unicode confirmed'
        decodedContents = contents.decode(coding)
    else:
        print 'unicode confirmed'
        decodedContents = contents.encode('utf-8')
    return decodedContents

def getChildrenContents(strings = ''):
    """
    return the key nodes from the downloaded url resources
    """
    strings = strings.rstrip()
    tree = ElementTree.fromstring(strings)
    root = tree.getroot()
    print root.tag
#    for node in tree.getchildren():
#        print node.tag, node.attrib

if __name__ == '__main__':


    urlContent = requestUrlResources()
    decodedContent = encodingRequestedConents(urlContent, 'ascii')
    print decodedContent
#
    k = getChildrenContents(decodedContent)
