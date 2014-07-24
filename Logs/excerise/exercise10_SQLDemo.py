__author__ = 'k22li'

import MySQLdb
import sys

CONST_DB_HOST = 'localhost'
CONST_DB_USER = 'root'
CONST_DB_PASSWD = '*Zhihui83'
CONST_DB_TABLE = 'nst_mtbf_aol3'

def connect():

    try:
        db = MySQLdb.connect(CONST_DB_HOST, CONST_DB_USER, CONST_DB_PASSWD, CONST_DB_TABLE)
        return db
    except MySQLdb.DatabaseError as e:
        print 'Connection to DB is unavailable, kindly check your host, user, passwd, table etc!'
        sys.exit(0)

def getCursor(db):

    return db.cursor()

def searchDB(db):

    cursor = getCursor(db)
    sql = 'SELECT * FROM test_case_table'

    cursor.execute(sql)
    results = cursor.fetchall()

    return results

def insert(db, sql):

#    caseID, featureGroup, feature, caseName, result = caseInfo
#    sql = "INSERT INTO mytable2 (CaseID, FeatureGroup, Feature, CaseName, Result) VALUES (\"%s\", \"%s\", \"%s\", \
#        \"%s\", \"%s\")" %(caseID, featureGroup, feature, caseName, result)

    try:
        cursor = db.cursor()
        cursor.execute(sql)

        db.commit()     #commit will operating with the DB connections, which would be a bit low efficient
    except MySQLdb.DatabaseError as e:
        print 'ERROR: Failed to insert! Reason: %s' %e
        db.rollback()

def updateDB(db, **kwargs):

    for key in kwargs:
        if key == 'Result':
            sql = "UPDATE mytable2 SET Result='%s' WHERE CaseID='%s'" %(kwargs['Result'], kwargs['CaseID'])
        elif key == 'CaseName':
            sql = "UPDATE mytable2 SET CaseName='%s' WHERE CaseID='%s'" %(kwargs['CaseName'], kwargs['CaseID'])
        else:
            print 'wrong inputs!'

#        print key, '---> ', kwargs[key]

        cursor = getCursor(db)
        cursor.execute(sql)
        db.commit()

def close(db):
    db.close()

if __name__ == '__main__':

    db = connect()
    updates = {'CaseID':'0000', 'Result': 'PASS', 'CaseName' : 'updated casename'}
    updateDB(db, **updates)
    for line in searchDB(db):
        print line

    close(db)
