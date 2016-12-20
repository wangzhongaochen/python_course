#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function


class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)

x = FirstClass()
y = FirstClass()
x.setdata("King Arthur")
y.setdata(3.1415926)
x.display()
y.display()

class SecondClass(FirstClass):
    def display(self):
        print('Current value = {0}'.format(self.data))

z = SecondClass()
z.setdata(42)
z.display()

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __mul__(self, other):
        self.data = self.data * other

a = ThirdClass("abc")
a.display()
b = a + 'xyz'
b.display()
a * 3
a.display()
