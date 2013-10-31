__author__ = 'k22li'

from xml.etree.ElementTree import ElementTree

class XMLParser(object):
    """
    parser the xml file, and return the needed info
    """
    def __init__(self, file = ''):
        """

        """
        self.srcFile = file
        self.tree = ElementTree()
        self.root = self.tree.parse(self.srcFile)

    def __call__(self, file = ''):
        """"""
#        self.__init__(file)
#        parser = self(file)
        attribDict = self._getTestCaseDetails()
        failureReason = self._getFailureReason()
        attribDict.update(failureReason)
        return attribDict

    def _getChildren(self):
        """
        return the children detected from the xml prasered, return in a list format
        """
        return self.root.getchildren()

    def _getTestCaseNode(self):
        """
        return the testcase node object
        """
        nodesList = self._getChildren()
        for node in nodesList:
            if 'testcase' == node.tag:
                return node
        else:
            return None

    def _getTestCaseDetails(self):
        """
        return the attributes from the testcase nodes
        """
        tcNode = self._getTestCaseNode()
        if tcNode is None:
            return None
        else:
            return tcNode.attrib

    def _getFailureReason(self):
        """
        get the failure reason from the testcase nodes
        """
        failureDict = {
            'error'     :   '',
            'traceback' :   ''
        }
        parentNode = self._getTestCaseNode()
        if parentNode is not None:
            if 'Failed' == parentNode.get('result'):
                errorNode = parentNode.find('error')
                tracebackNode = errorNode.find('traceback')
                failureDict['error'] = errorNode.get('reason')
                failureDict['traceback'] = tracebackNode.text
            else:
                failureDict['error'] = 'n/a'
                failureDict['traceback'] = 'n/a'
        return failureDict

if __name__ == '__main__':
    file = 'xml_data.xml'
    parser = XMLParser(file)
    attribDict = parser._getTestCaseDetails()
    failureReason = parser._getFailureReason()
    attribDict.update(failureReason)
    for k in attribDict.keys():
        print k, '------>', attribDict[k]