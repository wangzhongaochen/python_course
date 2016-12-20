#!/usr/bin/python
#-*- coding: UTF-8 -*-
from re_test_patterns import test_patterns

test_patterns('abbaaabbbbaaaaa',
        ['[ab]',    # either a or b
         'a[ab]+',  # a followed by one or more a or b
         'a[ab]+?', # a followed by one or more a or b,not greedy
         ])
