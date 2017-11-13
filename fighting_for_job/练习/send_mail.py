#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/2

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
__user = "853226549@qq.com"
__pwd = "obshehbpinorbeih"
__to = "853226549@qq.com"
msg = MIMEMultipart()
msg["Subject"] = "测试依稀"
msg["From"] = __user
msg["To"] = __to
#文字
part = MIMEText("nihao")
msg.attach(part)
#xlsx
part = MIMEApplication(open(r"C:\test\login.xlsx","rb").read())
part.add_header('Content-Disposition','attachment',filename = "qaf.xlsx")
msg.attach(part)
#jpg/pdf/mp3
# part = MIMEApplication(open(r"C:\test\login.jpg","rb").read())
# part.add_header('Content-Disposition','attachment',filename = "qaf.jpg")
# msg.attach(part)
try:
    s = smtplib.SMTP_SSL('http://stmp.qq.com',25)
    s.login(__user,__pwd)
    s.sendmail(__user,__to,msg.as_string())
    s.quit()
    print("success")
except smtplib.SMTPException as e:
    print(str(e))
