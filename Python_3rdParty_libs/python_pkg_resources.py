__author__ = 'k22li'

WRITE_SUPPORT = True
from os.path import split, isdir
from os import mkdir



def _bypass_ensure_directory(name, mode=0x1FF):  # 0777
    # Sandbox-bypassing version of ensure_directory()
    if not WRITE_SUPPORT:
        raise IOError('"os.mkdir" not supported on this platform.')
    dirname, filename = split(name)
    print '*'*80
    print dirname
    print filename

    if dirname and filename and not isdir(dirname):
        print '#'*80
        _bypass_ensure_directory(dirname)
        mkdir(dirname, mode)



if __name__  == '__main__':

    _bypass_ensure_directory(r'c:\evo_testfile\PYTHON\kkk\BBB')



#################################################################################################################################################
#RUN RESULT

#C:\apps\python27\python.exe C:/Users/k22li/workspace/gitHub/Python_Projects/python/Python_3rdParty_libs/python_pkg_resources.py
#********************************************************************************
#c:\evo_testfile\java
#kkk
#################################################################################
#********************************************************************************
#c:\evo_testfile
#java