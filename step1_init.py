#!/usr/bin/python
#-*- coding: UTF-8 -*-

from __future__ import print_function
class Person:
    #def __init__(self, name, job, pay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

if __name__ == '__main__':
    # self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=10000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
