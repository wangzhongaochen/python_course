#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def get_first_name(self):
        return self.name.split()[0]

def send_email(person):
    print('Dear {0}'.format(person.get_first_name()))

if __name__ == '__main__':
    bob = Person('Bob Smith', job='mgr', pay=10000)
    send_email(bob)
