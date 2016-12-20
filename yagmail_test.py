#!/usr/bin/python
#-*- coding: UTF-8 -*-

import yagmail
import smtplib
import datetime

def main():
    recipients = [{'name':'WANG Zhong', 'email':'wangzhong418@163.com'}, {'name':'HOU Xiaolin', 'email':'81711467@qq.com'}]
    data = 'send email test...'
    #now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with yagmail.SMTP(user='wangzhongaochen@163.com', password='wangxinyang+1=?', host='smtp.163.com', port='25', smtp_starttls=False) as yag:
        for rec in recipients:
            yag.send(rec['email'], "I now can send an attachment", data)

if __name__ == '__main__':
    main()
