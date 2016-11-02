#!/usr/bin/python
#-*- coding: UTF-8 -*-

import os
import shutil

source_file = os.path.realpath(__file__)
workspace = os.path.split(source_file)[0]
backup_dir = os.path.join(workspace,'backup')
if os.path.exists(backup_dir):
    shutil.rmtree(backup_dir)
os.mkdir(backup_dir)
shutil.copy(source_file,backup_dir)
