__author__ = 'k22li'


from ftplib import FTP

ftp = FTP()
ftp.connect(host='192.168.0.100', port=21)
ftp.login(user='lizhihui-kevin', passwd='*Zhihui83')
#ftp.retrlines('LIST')

print ftp.getwelcome()
print ftp.sendcmd('HELP')
print ftp.sendcmd('QUIT')