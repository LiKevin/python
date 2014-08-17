#    __author__ = 'k22li'
#
#    txt = '''
#    Alog.txt
#    10:00:00, <CallID>, Start VideoCall, B
#    10:00:27, <CallID>,Connected, B
#    10:02:32, <CallID>,Disconnected from other side, B
#
#
#    From user B sight, the log will be:
#
#    Blog.txt
#    10:00:03, <CallID>,Incoming Call , A
#    10:00:26, <CallID>,Received, A
#    10:02:31, <CallID>,Disconnected, A
#
#    '''
#
#    txt2= '''10:00:27, <CallID>,Connected, B'''
#
#    import re
#
#
#    start_patten = re.compile('(\d{2}:\d{2}:\d{2}),\s+<(\w+)>,\s?Start VideoCall\s?,\s+(\w)')
#    conn_patten = re.compile('(\d{2}:\d{2}:\d{2}),\s+<(\w+)>,\s?Connected\s?,\s+(\w)')
#    incom_patten = re.compile('(\d{2}:\d{2}:\d{2}),\s+<(\w+)>,\s?Incoming Call\s?,\s+(\w)')
#    rec_patten = re.compile('(\d{2}:\d{2}:\d{2}),\s+<(\w+)>,\s?Received\s?,\s?(\w)')
#    disconn_init_patten = re.compile('(\d{2}:\d{2}:\d{2}),\s+<(\w+)>,\s?Disconnected from other side\s?,\s+(\w)')
#    disconn_patten = re.compile('(\d{2}:\d{2}:\d{2}),,\s+<(\w+)>,\s?Disconnected\s?,\s+(\w)')
#
#    start_result = start_patten.search(txt)
#    incom_result = incom_patten.search(txt2)
#    conn_result = conn_patten.search(txt2)
#    disconn_init_result = disconn_init_patten.search(txt)
#
#    print start_result.group(1)
#    print conn_result.group()
#    #print disconn_init_result.group(0)
#
#    with open('txt', 'r') as f:
#        line = f.readline()
#        while line:
#            print line


print '>>> Dictionary print from "pattern" module: {}'.format(__builtins__)
print '>>> Type of __builtins__ from "pattern" module: {}'.format(type(__builtins__))


import __builtin__

greet('Cathy')