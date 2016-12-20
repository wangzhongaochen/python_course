#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
 
import sys
import os
import time
 
import pymysql
 
TEMPFILE = "/tmp/data.txt"
 
def get_conn(**kwargs):
    return pymysql.connect(host=kwargs.get('host', '127.0.0.1'),
            user=kwargs.get('user'),
            passwd=kwargs.get('passwd'),
            port=kwargs.get('port', 3306))
 
def get_info_from_database(conn):
    """
    In [14]: { row[0]:row[1] for row in rows if row[0] in ['Questions', 'Com_select', 'Com_insert', 'Com_update', 'Com_delete']}
    Out[14]:
    {'Com_delete': '324',
     'Com_insert': '2698658',
     'Com_select': '30528577',
     'Com_update': '8',
     'Questions': '62537046'}
    """
    items = ['Questions', 'Com_select', 'Com_insert', 'Com_update', 'Com_delete']
    sql = "show global status"
    with conn as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        return { row[0]: int(row[1]) for row in rows if row[0] in items }
 
 
def save_data_to_file(data):
    with open(TEMPFILE, 'a') as f:
        print(data['Questions'], data['Com_select'], data['Com_insert'], data['Com_update'], data['Com_delete'], sep='\t', file=f)
 
 
def collect_databse_info():
    conn = get_conn(user='wangzhong', passwd='wangzhong')
    previous_data = None
    while True:
        data = get_info_from_database(conn)
        save_data_to_file(data)
        if previous_data != None:
            print(data['Questions'] - previous_data['Questions'], data['Com_select'] - previous_data['Com_select'], data['Com_update'] - previous_data['Com_update'], data['Com_insert'] - previous_data['Com_insert'], data['Com_delete'] - previous_data['Com_delete'], sep='\t', file=sys.stdout)
            pass
        previous_data = data
        time.sleep(1)
 
 
def report_database_info():
    """'Questions', 'Com_select', 'Com_insert', 'Com_update', 'Com_delete'"""
    with open(TEMPFILE) as f:
        data = f.readlines()
    """
    In [5]: first.split()
    Out[5]: ['62568351', '30545170', '2698658', '8', '324']
    """
    first = data[0]
    last = data[-1]
 
    first_data = [ int(item) for item in first.split() ]
    last_data = [ int(item) for item in last.split() ]
    seconds = len(data)
 
    print('*' * 80)
    print("'Questions', 'Com_select', 'Com_insert', 'Com_update', 'Com_delete'")
    for first_item, last_item in zip(first_data, last_data):
        print((last_item - first_item) * 1.0 / seconds, end = '\t')
    print('*' * 80)
 
 
def main():
    # 避免在用户没有输入任何参数的时候，访问sys.argv[1]的时候索引越界
    sys.argv.append(None)
 
    if sys.argv[1] == 'start':
        if os.path.exists(TEMPFILE):
            os.remove(TEMPFILE)
        collect_databse_info()
    elif sys.argv[1] == 'report':
        if not os.path.exists(TEMPFILE):
            raise SystemExit('please run {0} start to collect database info'.format(sys.argv[0]))
        else:
            report_database_info()
    else:
        raise SystemExit('Usage: {0} start/report'.format(sys.argv[0]))

if __name__ == '__main__':
    main()
