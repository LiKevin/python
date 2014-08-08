__author__ = 'k22li'

#######################################################################################################################
# function implementations                                                                                            #
#######################################################################################################################

import re
from datetime import datetime

class Call_Log_Parser():
    '''
    for parsing the call logs and return the timestamps needed
    '''
    def __init__(self, log_file, call_id):
        self.log_file = log_file
        self.call_id = call_id
        # because __init__() can only return "None", \
        # so have to design this __call__() methods to return the value as below

    def __call__(self):
        '''calling'''
        return self.log_parser()

    def log_parser(self):

        call_id_pattern = re.compile('<(\d+)>') # pattern for getting the call_ids
        call_details = {}
        with open(self.log_file, 'r') as f:
            line_content = f.readline()
            while line_content:
                call_id_search = call_id_pattern.search(line_content)   # try to get the matching lines
                if call_id_search and self.call_id == call_id_search.group(1):  # ensure the needed Call_ID matching
                    info = [ info.strip() for info in line_content.split(',')]  # split the line by ","
                    call_details.update({info[2] : self.convert_to_time_obj(info[0])}) # store all info using dict

                # stop readline so long as all 3 times info collected, because of the large scale of logs -->saving time
                if 3 == len(call_details):
                    break   # FIXME: to confirm after this break, do we need to close this file handler manually????
                line_content = f.readline()
        return call_details

    def convert_to_time_obj(self, time_string):
        '''
        Convert the time_string to datetime object; Not Done Yet!!!
        '''
        time_obj = datetime.strptime(time_string, '%H:%M:%S')
        return time_obj

class Log_Analysis_Runner():

    def __init__(self, log1, log2, call_id):
        self.log1 = log1
        self.log2 = log2
        self.call_id = call_id
        # because __init__() can only return "None", \
        # so have to design this __call__() methods to return the value as below

    def __call__(self):
        '''start executing the runner'''
        return self.run()
        
    def run(self):
        try:
            call_details_1 = Call_Log_Parser(self.log1, self.call_id)()
            call_details_2 = Call_Log_Parser(self.log2, self.call_id)()

            if all((call_details_1, call_details_2)):   # ensure both timestamps existing, then start calculating
                self.call_durations = {}    # define the returns
                for detail in (call_details_1, call_details_2):
                    self.call_durations.update(detail)
                return [str(tim_obj) for tim_obj in \
                        [abs(self.call_durations['Start VideoCall'] - self.call_durations['Incoming Call']), \
                        abs(self.call_durations['Connected'] - self.call_durations['Received']), \
                        abs(self.call_durations['Disconnected'] - self.call_durations['Disconnected from other side']) \
                        ]   # timedelta obj could be convert to str directly via str()...
                    ]
            else:
                print('>>> Some call logs are missing, could not proceeding the analysing')
                return
        except (Exception, IndexError, AttributeError, ValueError) as error:
            print('>>> Error when proceeding the log analysis, reason: %s' %error)
            return

#######################################################################################################################
# test codes                                                                                                          #
#######################################################################################################################
if __name__ == '__main__':
    log_a = r'Alog.txt'
    log_b = r'Blog.txt'
    call_id = str(1023)
    duration_gap = Log_Analysis_Runner(log_a, log_b, call_id)
    print('The time gaps are: %s' %duration_gap())

    # Output:
    # The time gaps are: ['0:00:03', '0:00:01', '0:00:01']