#!/usr/bin/python
#-*- coding: UTF-8 -*-
import ConfigParser

# Requre values
try:
    parser = ConfigParser.SafeConfigParser()
    parser.read('allow_no_value.ini')
except ConfigParser.ParsingError,err:
    print 'Could not parse:',err

# Allow stand-alone option names
print '\n Trying again with allow_no_value=True'
parser = ConfigParser.SafeConfigParser(allow_no_value=True)
parser.read('allow_no_value.ini')
for flag in [ 'turn_feature_on','turn_other_feature_on' ]:
    print 
    print flag
    exists = parser.has_option('flags',flag)
    print '  has_option:',exists
    if exists:
        print '        get:',parser.get('flags',flag)
