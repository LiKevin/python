__author__ = 'k22li'

import csv


def readFromSpec(file):

    with open(file, 'r+') as reader:
        for line in reader.readlines():
            print line


if __name__=='__main__':

    fileLocation=r'C:\Users\k22li\workspace\gitHub\Python_Projects\python\Logs\mtbf_test_spec.xlsx'

    readFromSpec(file=fileLocation)