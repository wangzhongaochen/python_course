#!/usr/bin/python
#-*- coding: UTF-8 -*-


from __future__ import print_function

class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' %(key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self):
        return '[%s: %s]' %(self.__class__.__name__, self.gatherAttrs())

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

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

    tom = Manager('Tom Jones', 20000)
    tom.give_raise(0.1)
    print(tom)
