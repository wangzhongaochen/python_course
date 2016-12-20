#!/usr/bin/python
#-*- coding: UTF-8 -*-
from ConfigParser import SafeConfigParser
import glob

parser = SafeConfigParser()

candidates = ['does_not_exist.ini','also-does-not-exist.ini',
        'simple.ini','multisection.int',
        ]

found = parser.read(candidates)
missing = set(candidates) - set(found)

print 'Found config files:',sorted(found)
print 'Missing files     :',sorted(missing)
