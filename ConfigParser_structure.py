#!/usr/bin/python
#-*- coding: UTF-8 -*-
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('multisection.ini')

for section_name in parser.sections():
    print 'Section:',section_name
    print 'Options:',parser.options(section_name)
    for name,value in parser.items(section_name):
        print '    {0} = {1}'.format(name,value)
    print
