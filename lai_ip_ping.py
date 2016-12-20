#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function

import time
from threading import Thread
import subprocess
import logging

import logging
logging.basicConfig(filename='/tmp/ping_example.log',
            format='%(asctime)s %(levelname)-5.5s [%(name)s:%(lineno)s] %(message)s',
            level=logging.INFO)

LOG = logging.getLogger(__name__)


def execute_cmd(cmd):
    LOG.debug('ready to execute command : {0}'.format(cmd))
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        LOG.error("execute command ({0}) error ({1})".format(cmd, stderr))
        return p.returncode, stderr
    return p.returncode, stdout


def execute(cmd):
    return_code, _ = execute_cmd(cmd)
    return return_code == 0


def is_ip_reachable(ip):
    cmd = "ping -c 1 -t 2 {0}".format(ip)
    ret = execute(cmd)
    if ret:
        LOG.info("{0} is reachable".format(ip))
    else:
        LOG.error("{0} is unreacheable".format(ip))
    return ret


def main():
    with open('ip.list') as f:
        ips = [ line.strip() for line in f ]

    for ip in ips:
    #    is_ip_reachable(ip)
        t = Thread(target=is_ip_reachable, args=(ip,))
        t.start()


if __name__ == '__main__':
    main()
