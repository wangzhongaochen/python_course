#!/usr/bin/python
#-*- coding: UTF-8 -*-


from __future__ import print_function
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: {0}, {1}]'.format(self.name, self.pay)

class Manager(Person):

    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent + bonus)

if __name__ == '__main__':
    # self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=10000)
    print(bob)
    print(sue)

    print(bob.last_name(), sue.last_name())
    sue.give_raise(0.1)
    print(sue)

    tom = Manager('Tom Jones', 'mgr', 20000)
    tom.give_raise(0.1)
    print(tom)

