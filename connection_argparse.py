#!/usr/bin/python
#-*- coding: UTF-8 -*-
import argparse
import pymysql

def get_args():
    parser = argparse.ArgumentParser(add_help=True,conflict_handler='resolve')

    parser.add_argument('-h','--host',action="store")
    parser.add_argument('-P','--port',action="store",type=int)
    parser.add_argument('-u','--user',action="store")
    parser.add_argument('-p','--passwd',action="store")

    return parser.parse_args()

def get_conn():
    arglist = get_args()
    return pymysql.connect(host=arglist.host,
                           port=arglist.port,
                           user=arglist.user,
                           passwd=arglist.passwd)
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

