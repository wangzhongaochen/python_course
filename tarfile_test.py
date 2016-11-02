#!/usr/bin/python
#-*- coding: UTF-8 -*-

import tarfile
import os

print 'creating archive'
out = tarfile.open('tarfile_add.tar.gz',mode='w:gz')
try:
    out.add(os.getcwd())
finally:
    out.close()

os.mkdir('outdir')
t = tarfile.open('tarfile_add.tar.gz',mode='r:gz')
t.extractall('outdir')

