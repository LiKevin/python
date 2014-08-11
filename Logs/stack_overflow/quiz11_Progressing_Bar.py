__author__ = 'k22li'
########################################################################################################################
# Questions:
# search/ match/ findall from regular expression
# Fixme: key point:  search & match will stop when encountering with "\n" ; while findall() method last till end
########################################################################################################################

# demo 1
########################################################################################################################

def progress_bar_implementation_1():

    import sys
    import time
    print "#### START ####"
    for i in range(100):
        sys.stdout.write("[%s>%s] %s%%\r" % ('='*i, ' '*(100-i), (i+1)))
        time.sleep(0.05)
    #print ""
    sys.stdout.write('\n')
    sys.stdout.flush()  # flushing the stdout
    print "#### END ####"
    del sys
    del time

    try:
        print sys.version_info
    except UnboundLocalError as e:
        print '*'*100
        print '*'+'Error warning:  %s'.center(100-len(str(e)))%e+'*'
        print '*'*100

# demo 2
########################################################################################################################
def progress_bar_implementation_2():
    import sys
    import time

    print '*'*100
    for i in range( 100 ):
        time.sleep( 0.05 )
        sys.stdout.write( "File transfer progress :%3d%% percent complete!\r" %(i+1) )
        sys.stdout.flush()


if __name__ == '__main__':

    progress_bar_implementation_1()

    progress_bar_implementation_2()