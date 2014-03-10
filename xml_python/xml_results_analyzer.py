__author__ = 'k22li'

import xml.etree.ElementTree as ET
import os

class Filer():

    def __init__(self, resultDir = ''):

        self.dir = resultDir

    def findAllXmlSources(self):
        xml_files = []

        if not os.path.isdir(self.dir):
            print 'Invalid dir provided for fetching automation execution results!'
            return 0
        else:
            files = os.listdir(self.dir)
            for item in files:
                xml_files.append(item.rstrip())

            return xml_files, len(xml_files)


class XmlAnalyzer():

    def __init__(self, fileList = ''):
        self.fileList = fileList

    def getExecutionResultsFromXml(self, resultXml):

        with open(resultXml, 'r') as f:
            eletree = ET.parse(f)
            root = eletree.getroot()
            resNodes = root.getchildren()
            for node in resNodes:
                if node.tag == 'testcase':
                    return node.get('result'), node.get('subarea'), node.get('feature')

if __name__ == '__main__':

#    work_dir = r'C:\Users\k22li\Downloads\tools\Granite_Installation\Granite_ver1.3.6\test_sets\new_testset_results\xml'
    work_dir = r'C:\Users\k22li\1H-2014_Projects\RTAS\OnyxSS_DFT_Vodafone_WK07_18_02_Round 2_results\xml'
    F = Filer(work_dir)
    xmls, count = F.findAllXmlSources()

    analyzer = XmlAnalyzer(xmls)

    counter =0
    print 'Subarea', '\t', 'Feature', '\t', 'TestName', '\t', 'Result', '\t', 'Links'
    for xml in xmls:
        counter += 1
        xpath = os.path.join(work_dir, xml)
        result, subarea, feature = analyzer.getExecutionResultsFromXml(xpath)
        print subarea, '\t', feature, '\t', xml, '\t', result, '\t', 'file://'+xpath

    print counter