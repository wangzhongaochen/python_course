#!/usr/bin/python
#-*- coding: UTF-8 -*-

import logging
import threading
import time


log_filename='logging_example.log'
logging.basicConfig(filename=log_filename,
        level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
        )

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()
