#!/usr/bin/python
#-*- coding: UTF-8 -*-
import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock() - t
        return res
    return wrapper

def logging(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res
    return wrapper

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print "{0} has been used:{1}x".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper

@benchmark
@logging
@counter
def reverse_string(string):
    return reversed(string)

print reverse_string('hanlei')
print reverse_string('hanmeimei')
