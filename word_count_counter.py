#!/usr/bin/python
#-*- coding: UTF-8 -*-

from __future__ import print_function
from collections import Counter
import re

word_counts = Counter()
with open('vmstat.txt','rt') as f:
    for line in f:
        word_counts.update(re.findall('\w[a-zA-Z]{2,}\w',line))

for key,val in word_counts.most_common(9):
    print(key,':',val)
