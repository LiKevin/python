# -*- coding: utf-8 -*-
__author__ = 'k22li'


import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送方
sender = "lizhihui_kevin@163.com"
# 接收方
receiver = "lizhihui-kevin@live.com"

# 中文需要utf-8参数,不好使需要调整
# 在这里输入邮件标题 邮件内容

msg = MIMEText("service is down", 'plain', 'utf-8')

title = "service email"
msg['Subject'] = Header(title,'utf-8')

try:
    session = smtplib.SMTP()
    # 输入发送方的邮件服器名称, gmail需要指定端口:587
    session.connect("smtp.163.com")

    # 填写用户名和密码登录
    userName = "lizhihui_kevin@163.com"
    passwd = "*Zhihui83"
    session.login(userName, passwd)

    # 开始发送邮件
    session.sendmail(sender, receiver, msg.as_string())
    session.quit()
except Exception,e:
    print e
else:
    print "send mail success!"