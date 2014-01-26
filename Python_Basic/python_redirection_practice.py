__author__ = 'k22li'

import sys

class redirection:

    def _init_(self):
        self.buff=''
        self._console_=sys.stdout

    def write(self, output_stream):
        self.buff+=output_stream

    def to_console(self):
        sys.stdout=self._console_
    print self.buff

    def to_file(self, file_path):
        f=open(file_path,'w')
        sys.stdout=f
        print self.buff
        f.close()

    def flush(self):
        self.buff=''

    def reset(self):
        sys.stdout=self._console_

if __name__=="__main__":
    r_obj=redirection()

    sys.stdout=r_obj

    get output stream
    print 'hello'
    print 'there'
    redirect to console
    r_obj.to_console()
    redirect to file
    r_obj.to_file('out.log')
    flush buffer
    r_obj.flush()
    reset
    r_obj.reset()