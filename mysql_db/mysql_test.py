__author__ = 'k22li'

from mysql.connector import connection

class MySql(object):

    def __init__(self, user = '', password = '', database = ''):
        """login my sql"""

        self.user   = user
        self.password = password
        self.database   = database
        self.mysql = ''

    def _login(self):

        self.mysql = connection.MySQLConnection(user = self.user, password = self.password, database = self.database)
        print self.mysql.get_server_version()

    def _createAttribList(self, **kwargs):
        attrList = []
        assert len(kwargs), 'EMPTY ATTRIBUTE LIST PROVIDE, NOT POSSIBLE TO CREATE NEW TABLE WITHOUT ANY ATTRIBS!'
        for attrTuple in kwargs.items():
            attrItem = ' '.join(attrTuple)
            attrList.append(attrItem)

        return ', '.join(tuple(attrList))

    def _createNewTable(self, tableNam = '', **kwargs):
        """
        create new table with name as tableNam
        """
        attribs = self._createAttribList(**kwargs)
        print attribs
        self.mysql.cmd_query("SHOW TABLES;")
        existTables = self.mysql.get_rows()[0]
        print 'THE EXISTING TABLES IN THE CURRENT DB ARE: %s' %existTables
        if not tableNam in existTables:
            self.mysql.cmd_query('CREATE TABLE %s(%s)'%(tableNam, attribs))
        else:
            print 'ALREADY THE TABLE WITH THE SAME NAME IN THE DB!'

    def _insertValues(self, tableNam = '', params = []):
        value = tuple(params)
        try:
            self.mysql.cmd_query('INSERT INTO %s VALUES%s'%(tableNam, value))
            self.mysql.cmd_query('COMMIT')
        except:
            print 'FAILED TO INSERT THE TEST VALUES TO THE DATABASE!'

    def _showContents(self, tableNam = ''):
        try:
            self.mysql.cmd_query('SELECT * FROM %s' %tableNam)
            counter = 0
            for line in self.mysql.get_rows()[0]:
                counter += 1
                print '****', line, counter
        except:
            print 'faile to load the test database'

    def _cleanDatabase(self, tableNam ='', condition = ()):
        k, v = condition
        print k, v
        try:
            self.mysql.cmd_query('DELETE FROM %s WHERE %s = "%s";'%(tableNam, k, v))
            self.mysql.cmd_query('COMMIT')
        except:
            print 'Failed to clean up the DATABASE'

if __name__ == "__main__":
    attribDict = {'FeatureGroup' : 'VARCHAR (160)', 'Feature' : 'VARCHAR(60)', 'CaseName' : 'VARCHAR(256)', 'TestResult' : 'VARCHAR(20)', 'ExecDate' : 'DATETIME'}
    values = ['Calling people', 'call control', 'create a MO call', 'Passed', '2013-11-02']
    t = MySql(user = 'root', password = '@Zhihui83', database = 'test')

    t._login()

    t._showContents(tableNam = 'test_table')
    t._insertValues(tableNam = 'test_table', params = values)
    t._showContents(tableNam = 'test_table')
    t._cleanDatabase(tableNam = 'test_table', condition = ('Feature', 'Calling people'))
    t._showContents(tableNam = 'test_table')