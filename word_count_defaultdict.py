#!/usr/bin/python
#-*- coding: UTF-8 -*-

from __future__ import print_function
import re
from collections import defaultdict

d = defaultdict(int)
with open('vmstat.txt','rt') as f:
    for line in f:
        words = re.findall('\w[a-zA-Z]{2,}\w',line)
        for word in words:
            d[word] += 1

result = sorted(zip(d.values(),d.keys()),reverse=True)[:9]
for val,key in result:
    print(key,':',val)
