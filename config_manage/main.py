#!/usr/bin/python
#-*- coding: UTF-8 -*-
from ConfigParser import SafeConfigParser
import os.path
import traceback

def init_storage_config(main_dir,env):
    source_dir = os.path.join(main_dir,'config',env)
    target_dir = os.path.join(main_dir,'storage','config')
    target_files = [ os.path.join(target_dir,item) for item in os.listdir(target_dir) ]
    source_files = [ os.path.join(source_dir,item) for item in os.listdir(source_dir) ]

    for target,source in zip(target_files,source_files):
        with open(target,'w') as t,open(source,'r') as s:
            t.write(s.read())

def init_runtime_env():
    parser = SafeConfigParser(allow_no_value=True)
    try:
        parser.read('env.cfg')
        env = parser.get('env','environment')
        main_dir = os.path.split(os.path.realpath(__file__))[0]
        init_storage_config(main_dir,env)
    except Exception, e:
        traceback.format_exc()
        raise Exception("init environment error: {0}".format(e))

if __name__ == '__main__':
    init_runtime_env()
