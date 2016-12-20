#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
import re


input = raw_input("Enter an ip address: ")
m = re.match('^([1-9]|[1-9][0-9]|1[0-9]{2}|2[01][0-9]|22[0-3])(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])){2}\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])$', input)

if m:
    print("True")
else:
    print("False")
