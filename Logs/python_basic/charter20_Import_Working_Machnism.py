# -*- coding: utf-8 -*-
#__author__ = 'k22li'    # this declaration should be removed if the "from __future__ import " existing

######################################################################################################################
# function implementations
# purpose is to:
# try to understand how this "Import" vs "__import__" working with
########################################################################################################################

# demo 1
########################################################################################################################

def import_from(name):
    try:
        return __import__(name, fromlist=[''])
    except ImportError, err:
        print('>>> Error when importing %s, reason: %s' %(name, err))
        try:
            m_pos = name.rfind('.')
            mdl = __import__(name[:m_pos], fromlist=[''])
            return   getattr(mdl, name[m_pos+1:])
        except ImportError, err:
            print('>>> Error when importing %s, reason: %s' %(name[:m_pos], err))
        except AttributeError, err:
            print('>>> Error when importing %s, reason: %s' %(name[m_pos+1:], err))
        except RuntimeError:
            print('>>> Runtime error here...')


if __name__ == '__main__':

    print import_from('contextlib.contextmanager')