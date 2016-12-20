#!/usr/bin/python
#-*- coding: UTF-8 -*-
from re_test_patterns import test_patterns

test_patterns('This is some text -- with punctuation.',
        ['[a-z]+',      # sequences of lower case letters
         '[A-Z]+',      # sequences of upper case letters
         '[a-zA-Z]+',   # sequences of lower or upper case letters
         '[A-Z][a-z]+'  # one upper case letter followed by lower case letters
            ])
