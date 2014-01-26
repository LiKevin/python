__author__ = 'k22li'

import random

def produceValidSmsRecipients(amount = 20):

    prefix = '+861370313'
    recipients = [prefix+str(random.choice(range(0,9999))).zfill(4) for i in xrange(amount)]
    return recipients


print produceValidSmsRecipients(20)