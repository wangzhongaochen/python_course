#!/usr/bin/python
#-*- coding: UTF-8 -*-

from ConfigParser import SafeConfigParser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib, mimetypes
import psutil

# Contacts:name、address、birthday、phone、email
class Contacts:
    def __init__(self, name, address, birthday, phone, email):
        self.name = name
        self.address = address
        self.birthday = birthday
        self.phone = phone
        self.email = email

def get_all_monitor_info():
    return ('CPU  [{0:.2%}]\n'.format(psutil.cpu_percent(interval=2)) +
            'MeM  [{0:.2%}]\n'.format(psutil.virtual_memory().percent / 100) +
            'SWAP [{0:.2%}]\n'.format(psutil.swap_memory().percent / 100) +
            ' /   [{0:.2%}]'.format(psutil.disk_usage('/').percent / 100))

def send_email(parser, fro, to_addrs, subject, text):
    msg = MIMEMultipart()
    msg['From'] = fro
    msg['To'] = ', '.join(to_addrs)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    smtp = smtplib.SMTP()
    smtp.connect(parser.get('server', 'name'), parser.getint('server', 'port'))
    smtp.login(parser.get('server', 'username'), parser.get('server', 'passwd'))
    smtp.sendmail(fro, to_addrs, msg.as_string())
    smtp.close()

if __name__ == '__main__':
    parser = SafeConfigParser(allow_no_value=True)
    parser.read('server.ini')
    wangzhong = Contacts('wangzhong', 'xicheng beijing', '19001231', '15600000000', '81711467@qq.com')
    wangzhong2 = Contacts('wangzhong2', 'xicheng beijing', '19001231', '15600000000', 'wangzhong418@163.com')
    to_addrs = [ contact.email for contact in (wangzhong, wangzhong2) ]
    all_monitor_info = get_all_monitor_info()
    send_email(parser, parser.get('server', 'username'), to_addrs, 'Monitor info!', all_monitor_info)
