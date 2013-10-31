__author__ = 'k22li'
import os
import urllib
from zipfile import ZipFile
from python_xml_praser import XMLParser

#path = r'http://becim014.rnd.nokia.com:8081/job/Granite-Rfa-regression-test-lanaiSS/107/artifact/test_results/test_results/xml'
class XMLResult(object):
    """
    #    def __init__(self, pNam = '', jobNum = '', tarDir = ''):
    """
    def __init__(self, pNam = '', jobNum = '', tarDir = ''):
        print pNam, jobNum, tarDir
        jobNum = int(jobNum)
        self.tarDir = tarDir
#        self.path = r'http://becim014.rnd.nokia.com:8081/job/Granite-Rfa-regression-test-%s/%d/artifact//test_results/xml/*zip*/xml.zip'%(pNam, jobNum)
        self.path = r'http://becim014.rnd.nokia.com:8081/job/Granite-Rfa-regression-test-%s/%d/artifact/test_results/xml/*zip*/xml.zip'%(pNam, jobNum)

    def __call__(self, **kwargs):
        """ """
        failureResults = []
        caseList = self._extractFromZipFile(tarDir = self.tarDir)
        caseList = [os.path.join(self.tarDir, 'xml', item) for item in caseList]
        for item in caseList:
#            print item
            attributes = XMLParser(file = item)

            k = attributes(file = item)
#            print k
            if 'Failed' == k['result']:
                k.update({'hyperlink' : item})
                failureResults.append(k)

        return failureResults

    def _retrieveXMLToLocal(self):
        """
        return the local temp zip file name
        """
        cachedZip = urllib.urlretrieve(self.path)[0]
        return cachedZip

    def _dumpNameListFromZipFile(self):
        xmlsList = []
        cachedZip = self._retrieveXMLToLocal()
        with ZipFile(cachedZip, 'r') as myZip:
            xmls = myZip.namelist()
            if 'xml/' in xmls:
                xmls.remove('xml/')

            for xmlNam in xmls:
                xmlsList.append(os.path.join(cachedZip, xmlNam))
        return xmlsList

    def _extractFromZipFile(self, tarDir = ''):
        """

        """
        self.zipFile = self._retrieveXMLToLocal()
        with ZipFile(self.zipFile, 'r') as myZip:
            myZip.extractall(tarDir)

        xmlDir = os.path.join(tarDir, 'xml')
        if os.path.isdir(xmlDir):
            return os.listdir(xmlDir)
        else:
            return None

if __name__ == '__main__':

#    tarDir = os.path.join('C:\\', 'Temp', 'test_result')
#    failureResults = []
#    xml = XMLResult(pNam = 'orionDS', jobNum = '222')
#    kList = xml._dumpNameListFromZipFile()
#
#    caseList = xml._extractFromZipFile(tarDir = tarDir)
#    caseList = [os.path.join(tarDir, 'xml', item) for item in caseList]
#    for item in caseList:
##        print item
#        attributes = XMLParser(file = item)
#
#        k = attributes(file = item)
#        if 'Failed' == k['result']:
#            failureResults.append(k)
##            print k['id'], '    --->    ', k['error']
    tarDir = os.path.join('C:\\', 'Temp', 'test_result')
    Params = {'pNam' : 'lanaiSS', 'jobNum' : '107', 'tarDir' : tarDir}
    #    Params = ['lanaiSS', 107, tarDir]

    t = XMLResult(**Params)
    resList = t(**Params)
    print resList