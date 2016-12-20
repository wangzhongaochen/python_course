#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
from datetime import datetime

def log(username):
    def decorated(f):
        def wrapper(*args, **kwargs):
            start = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
            print(username, "call the functiton...")
            print("Function starting at {0}\n".format(start))
            print("Function content:")
            res = f(*args, **kwargs)
            stop = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
            print("\nFunction stoped at {0}".format(stop))
            return res
        return wrapper
    return decorated

@log('Clinton')
def say_hi(name):
    print('hello, {0}'.format(name))

say_hi('wangzhong')
