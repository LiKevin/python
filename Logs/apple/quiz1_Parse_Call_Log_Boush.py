#!/usr/bin/env python

import os
import time
import datetime

log_base_name = 'log.txt'
activates = {'Start VideoCall': 'Incoming Call',
             'Connected': 'Received',
             'Disconnected from other side': 'Disconnected'}
gap = []

class LogAnalyzer(object):
    def __init__(self, guid, sender, receiver):
        self.guid     = guid
        self.sender   = sender
        self.receiver = receiver
        self.content  = {}

    def convert_string_time(self, str_time):
        t = time.strptime(str_time, "%H:%M:%S")
        sec_tot = datetime.timedelta(hours   = t.tm_hour,
            minutes = t.tm_min,
            seconds = t.tm_sec).total_seconds()
        return sec_tot

    def get_gap(self, start_time, end_time):
        return int(
            abs(
                self.convert_string_time(start_time) - self.convert_string_time(end_time)
            )
        )

    def analyer(self):
        _sender = self.sender + log_base_name
        _receiver = self.receiver + log_base_name
        sender_contents = []
        receiver_contents = []
        if not os.path.exists(_sender):
            raise Exception('Error: Log file %s is not existing' % _sender)
        if not os.path.exists(_sender):
            raise Exception('Error: Log file %s is not existing' % _sender)
            # Handle log files
        try:
            fp_sender = open(_sender, 'r')
            fp_receiver = open(_receiver, 'r')
            sender_line = fp_sender.readline().strip('\n')
            receiver_line = fp_receiver.readline().strip('\n')
            while sender_line and receiver_line:
                sender_contents = [item.strip() for item in sender_line.split(',')]
                receiver_contents = [item.strip() for item in receiver_line.split(',')]
                if sender_contents[1] != receiver_contents[1]:
                    sender_line = fp_sender.readline()
                    receiver_line = fp_receiver.readline()
                    continue
                if sender_contents[1] != self.guid:
                    sender_line = fp_sender.readline()
                    receiver_line = fp_receiver.readline()
                    continue
                if receiver_contents[2] != activates[sender_contents[2]] or\
                   sender_contents[3] != self.receiver or\
                   receiver_contents[3] != self.sender:
                    raise Exception('Those two log files not matched.\n\
                                     Maybe some log missing.')
                gap.append(self.get_gap(sender_contents[0], receiver_contents[0]))
                sender_contents = []
                receiver_contents = []
                sender_line = fp_sender.readline()
                receiver_line = fp_receiver.readline()
        except Exception as err:
            raise Exception('IOError: %s' % err)
        else:
            pass
        finally:
            fp_sender.close()
            fp_receiver.close()

# Test
if __name__ == '__main__':
    tester = LogAnalyzer('1023', 'A', 'B')
    tester.analyer()
    print(gap)