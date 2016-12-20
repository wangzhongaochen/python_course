#!/usr/bin/python
#-*- coding: UTF-8 -*-
from util import execute
from multiprocessing import Pool
import time
import logging


LOG_FILE = 'logging.out'
logging.basicConfig(filename=LOG_FILE,
                    level=logging.DEBUG,
                    )

def get_ip_list():
    with open('ip.list','r') as f:
        return [ ip.strip() for ip in f]

def ip_ping(ip):
    if execute('ping -c 1 {0}'.format(ip)):
        logging.debug('ip {0} is alive.'.format(ip))
    else:
        logging.debug('ip {0} is not alive.'.format(ip))

def single_thread_ping():
    ip_list = get_ip_list()
    start = time.time()
    for ip in ip_list:
        ip_ping(ip)
    end = time.time()
    logging.debug('single thread ping consume {0}s'.format(end - start))

def multi_threads_ping():
    ip_list = get_ip_list()
    pool = Pool(10)
    start = time.time()
    pool.map(ip_ping, ip_list)
    end = time.time()
    logging.debug('multi threads ping consume {0}s'.format(end - start))

if __name__ == '__main__':
    single_thread_ping()
    multi_threads_ping()
