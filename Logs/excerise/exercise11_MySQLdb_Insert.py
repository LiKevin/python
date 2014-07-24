__author__ = 'k22li'


from exercise10_SQLDemo import *
import csv

CONST_CASE_CSV = r'C:\Users\k22li\AoL\scripting\NST_MTBF_CASE_SUMMARY_v1.0.csv'

def caseInfoUpdate():

#    connect to database
    db = connect()

    with open(CONST_CASE_CSV, 'rb') as cf:
        spamReader = csv.reader(cf)
        for line in spamReader:
            if not line[0].startswith('CASE') and not line[0] == '':
                case_id, feature_group, feature, case_name, auto_script_file, author = line

                sql = "INSERT INTO test_case_table(CASE_ID, FEATURE_GROUP, FEATURE, CASE_NAME, AUTO_SCRIPT_FILE, \
                        AUTHOR) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" \
                        %(case_id, feature_group, feature, case_name, auto_script_file, author)
                insert(db,sql)

    results = searchDB(db)
    for item in results:
        print item

    close(db)



if __name__ == '__main__':

    caseInfoUpdate()