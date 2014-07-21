__author__ = 'k22li'

import io


def bufferWritting():

    str_1 = 'hello Kevin!'

    writer = io.BufferedWriter(str_1)

    writer.flush()



if __name__=='__main__':

    bufferWritting()
