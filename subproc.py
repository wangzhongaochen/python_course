#!/usr/bin/python
#-*- coding: UTF-8 -*-

import subprocess

def execute_cmd(cmd):
    p = subprocess.Popen(cmd,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout

dats = execute_cmd('cat /etc/passwd')

with open('userinfo.txt','w') as f:
    for item in dats[1].strip('\n').split('\n'):
        items = item.split(':')
        try:
            f.write("{name},{home},{shell}\n".format(name=items[0],home=items[5],shell=items[6]))
        except IndexError:
            f.write("{name},{home},{shell}\n".format(name=items[0],home=items[5]))
