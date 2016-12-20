#!/usr/bin/python
#-*- coding: UTF-8 -*-
import functools

def is_admin(f):

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs.get("username") != 'admin':
            raise Exception("This user is not allowed to get food.")
        return f(*args, **kwargs)
    return wrapper

def foobar(username = 'someone'):
    """Do crazy stuff"""
    pass

@is_admin
def barfoo(username = 'someone'):
    """Do crazy stuff"""
    pass

print foobar.func_doc
print foobar.__name__
print barfoo.func_doc
print barfoo.__name__
