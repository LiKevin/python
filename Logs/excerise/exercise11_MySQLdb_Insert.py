__author__ = 'k22li'


from exercise10_SQLDemo import *
import csv

CONST_CASE_CSV = r'C:\Users\k22li\AoL\scripting\NST_MTBF_CASE_SUMMARY_v1.0.csv'

def caseInfoUpdate():

#    connect to database
    db = connect()

#    obtain all those existing case list
    exist_case = getExistingCaseList(db)

    with open(CONST_CASE_CSV, 'rb') as cf:
        spamReader = csv.reader(cf)
        for line in spamReader:
            if not line[0].startswith('CASE') and not line[0] == '':
                case_id, feature_group, feature, case_name, auto_script_file, author = line
                if case_id in exist_case:
                    pass
                else:
                    sql = "INSERT INTO test_case_table(CASE_ID, FEATURE_GROUP, FEATURE, CASE_NAME, AUTO_SCRIPT_FILE, \
                            AUTHOR) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" \
                            %(case_id, feature_group, feature, case_name, auto_script_file, author)
                    insert(db,sql)

    sql_search_all = 'SELECT * FROM test_case_table;'
    results = searchDB(db, sql_search_all)
    for item in results:
        print item

    close(db)

def getExistingCaseList(db):

    sql_check =  'SELECT %s FROM test_case_table;' %("CASE_ID")
    avail_case_id = searchDB(db, sql_check)
    exist_case = [ ele[0] for ele in avail_case_id ]
    return exist_case

if __name__ == '__main__':
    caseInfoUpdate()