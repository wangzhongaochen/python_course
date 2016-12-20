#!/usr/bin/python
#-*- coding: UTF-8 -*-
import re

text = 'abbaaabbbbaaaa'
pattern = 'ab'

for match in re.findall(pattern, text):
    print 'Found "%s"' % match
