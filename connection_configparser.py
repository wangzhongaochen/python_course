#!/usr/bin/python
#-*- coding: UTF-8 -*-
from ConfigParser import SafeConfigParser
import pymysql

def get_conn(**kwargs):
    parser = SafeConfigParser(allow_no_value=True)
    parser.read('my.ini')
    return pymysql.connect(host=parser.get('mysql','host'),
                           port=parser.getint('mysql','port'),
                           user=parser.get('mysql','user'),
                           passwd=parser.get('mysql','passwd'))
def main():
    conn = get_conn()
    try:
        with conn as cur:
            cur.execute('show databases;')
            rows = cur.fetchall()
            for row in rows:
                print row
    finally:
        conn.close()

if __name__ == '__main__':
    main()
