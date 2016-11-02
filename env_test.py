#!/usr/bin/python
#-*- coding: UTF-8 -*-

import os

print 'Initial value:', os.environ.get('TESTVAR',None)
print 'Child process:'
os.system('echo $TESTVAR')

os.environ['TESTVAR'] = 'THIS VALUE WAS CHANGED'

print
print 'Changed value:', os.environ['TESTVAR']
print 'Child process:'
os.system('echo $TESTVAR')

del os.environ['TESTVAR']

print
print 'Removed value:',os.environ.get('TESTVAR',None)
print 'Child process:'
os.system('echo $TESTVAR')
