__author__ = 'k22li'

class CasesSwap():
    """
    reverse the cases of each letters in the string provide
    """

    def __init__(self, rawString):
        """
        initialize local string
        """
        self.rawStr = rawString

    def caseSwap(self):
        """
        reverse the cases for each letters
        """
        return  self.rawStr.swapcase()

    def strJustification(self, orientation='left', width=8):
        """
        do string justification and return the copy of the justified string
        """
        if orientation.lower() == 'right':
            return self.rawStr.rjust(width, '*')
        elif orientation.lower() == 'right':
            return self.rawStr.ljust(width, '*')
        else:
            return self.rawStr.center(width, '*')

if __name__ == '__main__':

    CR = CasesSwap('abCDefGH')
    print CR.caseSwap()

    print CR.strJustification(orientation='center', width=20)